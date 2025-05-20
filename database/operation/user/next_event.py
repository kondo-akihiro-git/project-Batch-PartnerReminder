from database.connection import get_connection
from datetime import date, timedelta

def get_users_with_event_tomorrow():
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
        SELECT u.email, u.name, n.date
        FROM NextEventDay n
        INNER JOIN Users u ON u.id = n.user_id
        WHERE n.date = %s
    """
    # tomorrow = date.today() + timedelta(days=1)

    tomorrow = date.today() + timedelta(days=1)
    cur.execute(query, (tomorrow,))
    rows = cur.fetchall()
    
    cur.close()
    conn.close()

    # 結果は [(email, name, date), ...] のリスト形式
    return rows
