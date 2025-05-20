
from datetime import date, timedelta

from database.connection import get_connection


def get_full_data(user_email: str):
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT m.id
        FROM Meetings m
        INNER JOIN user_meetings um ON m.id = um.meeting_id
        INNER JOIN Users u ON um.user_id = u.id
        WHERE u.email = %s
        ORDER BY m.date DESC
        LIMIT 1
    """
    cur.execute(query, (user_email,))
    result = cur.fetchone()
    meeting_id = result[0] if result else None

    partner_points = []
    todo_text = ""

    if meeting_id:
        # PartnerGoodPoints
        cur.execute("""
            SELECT good_point FROM PartnerGoodPoints
            WHERE meeting_id = %s
        """, (meeting_id,))
        partner_points = [row[0] for row in cur.fetchall()]

        # TodoForNext（最新1件）
        cur.execute("""
            SELECT todo FROM TodoForNext
            WHERE meeting_id = %s
            ORDER BY id DESC
            LIMIT 1
        """, (meeting_id,))
        todo = cur.fetchone()
        todo_text = todo[0] if todo else ""

    cur.close()
    conn.close()

    return partner_points, todo_text