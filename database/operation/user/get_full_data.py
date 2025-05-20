
from datetime import date, timedelta

from database.connection import get_connection


def get_full_data(user_email: str):
    conn = get_connection()
    cur = conn.cursor()

    # ユーザーの関連する全MeetingのIDと日付を取得（日付降順）
    query = """
        SELECT m.id, m.date
        FROM Meetings m
        INNER JOIN user_meetings um ON m.id = um.meeting_id
        INNER JOIN Users u ON um.user_id = u.id
        WHERE u.email = %s
        ORDER BY m.date DESC
    """
    cur.execute(query, (user_email,))
    meeting_rows = cur.fetchall()  # [(meeting_id, date), ...]

    partner_points = []
    todo_text = ""

    if meeting_rows:
        meeting_ids = [row[0] for row in meeting_rows]

        # PartnerGoodPointsは全Meetingからまとめて取得
        format_ids = ','.join(['%s'] * len(meeting_ids))
        cur.execute(f"""
            SELECT good_point FROM PartnerGoodPoints
            WHERE meeting_id IN ({format_ids})
            AND good_point <> ''
        """, meeting_ids)
        partner_points = [row[0] for row in cur.fetchall()]

        # 最新Meeting（日付が最大）のIDを取得
        latest_meeting_id = meeting_rows[0][0]

        # そのMeetingのTodoForNextの最新1件をID降順で取得（複数登録されている可能性を考慮）
        cur.execute("""
            SELECT todo FROM TodoForNext
            WHERE meeting_id = %s
            ORDER BY id DESC
            LIMIT 1
        """, (latest_meeting_id,))
        todo = cur.fetchone()
        todo_text = todo[0] if todo else ""

    cur.close()
    conn.close()

    return partner_points, todo_text
