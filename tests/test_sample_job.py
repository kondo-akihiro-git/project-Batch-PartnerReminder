from app.jobs.sample_job import run_sample_job

def test_run_sample_job(capsys):
    run_sample_job()
    captured = capsys.readouterr()
    assert "Running sample job" in captured.out
