# run_api.py
from fastapi import FastAPI
from app.jobs.main_job import main_job
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def execute():
    return {"status": "batch executed"}

@app.get("/run-job")
def run_job():
    main_job()
    return {"status": "Job executed"}
