from some_db import DB

def test_db():
    # setup: connect to db
    db = DB()

    result = db.some_action()
    assert result == 42

    # teardown: close db
    db.close()

