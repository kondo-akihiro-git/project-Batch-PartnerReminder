from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs.main_job import main_job
import os
from dotenv import load_dotenv

load_dotenv()

def init_scheduler():
    scheduler = BackgroundScheduler()

    interval_seconds = int(os.getenv("SCHEDULER_INTERVAL_SECONDS", "10"))

    # 現在の日付がデートの前日か判定してメール送信するジョブ
    scheduler.add_job(main_job, 'interval', seconds=interval_seconds, id='main_job')

    scheduler.start()
    return scheduler
