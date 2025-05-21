from email.mime.text import MIMEText
import logging
import smtplib
from database.operation.user.get_full_data import get_full_data
import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルを読み込む


SMTP_HOST = os.getenv("SMTP_HOST", "localhost")
SMTP_PORT = int(os.getenv("SMTP_PORT", 1025))
SMTP_FROM = os.getenv("EMAL_FROM", "noreply@example.com")

# ログの基本設定
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def send_email(to_email: str, name: str, date_str: str):
    logging.info(f"'{name}' さんのメールアドレス（{to_email}）にメール送信処理を実行中")

    # 追加データ取得
    partner_points, todo_text = get_full_data(to_email)

    # メール本文作成
    body = f"{name} さん\n\n明日({date_str})にデートの予定があります。\n忘れずに準備をしてくださいね。\n\n"

    if partner_points:
        body += "◾️相手のいいところ\n"
        # partner_pointsはリストなので、改行は要素間に1つだけ入れる形で結合
        body += "\n".join(partner_points) + "\n\n"

    if todo_text:
        body += "◾️次回取り組むこと\n"
        body += todo_text + "\n\n"

    body += "リマインドは以上です。頑張ってください。"

    msg = MIMEText(body)
    msg["Subject"] = "【リマインド】明日のデート予定について"
    msg["From"] = SMTP_FROM
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.send_message(msg)
        logging.info("メールの送信完了")
    except Exception as e:
        logging.error(f"メール送信中にエラーが発生しました: {e}")