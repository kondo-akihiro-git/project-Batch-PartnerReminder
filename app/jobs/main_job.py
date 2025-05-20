from email.mime.text import MIMEText
import logging
from datetime import datetime
import smtplib
from database.operation.user.next_event import get_users_with_event_tomorrow

# ログの基本設定
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def send_email(to_email: str, name: str, date_str: str):
    logging.info(f"'{name}' さんのメールアドレス（{to_email}）にメール送信処理を実行中")

    subject = "【通知】明日のデート予定について"
    body = f"{name} さん\n\n明日({date_str})にデートの予定があります。\n忘れずに準備をしてくださいね。\n\nよろしくお願いいたします。"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "noreply@example.com"
    msg["To"] = to_email

    try:
        # 本番環境に合わせてSMTPサーバーやポートを修正してください
        with smtplib.SMTP("localhost", 1025) as server:
            server.send_message(msg)
        logging.info("メールの送信完了")
    except Exception as e:
        logging.error(f"メール送信中にエラーが発生しました: {e}")

def main_job():
    logging.info("--------------------バッチ処理を開始します--------------------")
    
    try:
        logging.info("明日の予定があるユーザーを取得中...")
        users = get_users_with_event_tomorrow()

        if not users:
            logging.info("明日デートの予定があるユーザーはいません。処理を終了します。")
            return

        logging.info(f"{len(users)}件のユーザーに対してメール送信処理を開始します。")
        for i, (email, name, date_val) in enumerate(users, 1):
            date_str = date_val.strftime('%Y-%m-%d')
            send_email(email, name, date_str)

    except Exception as e:
        logging.error(f"ユーザー情報の取得またはメール送信中にエラーが発生しました: {e}")

    finally:
        logging.info("-----------------一連のバッチ処理が完了しました------------------")

if __name__ == "__main__":
    main_job()
