from some_db import DB


def test_db():
    # setup: connect to db
    db = DB()

    result = db.some_action()

    # teardown: close db
    db.close()

    assert result == 42
