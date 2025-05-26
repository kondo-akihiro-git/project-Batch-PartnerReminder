from app.jobs.main_job import main_job
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

if __name__ == "__main__":
    main_job()
