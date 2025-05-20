from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs.main_job import main_job

def init_scheduler():
    scheduler = BackgroundScheduler()

    # 現在の日付がデートの前日か判定してメール送信するジョブ
    scheduler.add_job(main_job, 'interval', seconds=10, id='main_job')

    scheduler.start()
    return scheduler
