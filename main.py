from app.scheduler import init_scheduler
import time

if __name__ == "__main__":
    scheduler = init_scheduler()
    print("Scheduler started. Running jobs...")
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler shut down.")
