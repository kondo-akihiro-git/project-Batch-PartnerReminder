from app.jobs.main_job import main_job

def test_main_job(capsys):
    main_job()
    captured = capsys.readouterr()
    assert "明日デートの予定があるユーザーはいません" in captured.out
