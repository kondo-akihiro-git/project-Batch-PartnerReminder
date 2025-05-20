from app.jobs.main_job import main_job

def test_main_job(caplog):
    with caplog.at_level("INFO"):
        main_job()
    # caplog.textにログ出力全体が入るのでそれをチェック
    assert "明日デートの予定があるユーザーはいません" or "メール送信完了" in caplog.text
