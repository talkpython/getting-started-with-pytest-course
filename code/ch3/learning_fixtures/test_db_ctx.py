from contextlib import closing
from some_db import DB


def test_db():
    with closing(DB()) as db:
        result = db.some_action()
        assert result == 42
