from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs.sample_job import run_sample_job

def init_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_sample_job, 'interval', seconds=10, id='sample_job')
    scheduler.start()
    return scheduler
