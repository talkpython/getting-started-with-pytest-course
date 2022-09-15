import pytest

from some_db import DB


@pytest.fixture()
def db():
    db = DB()  # setup
    yield db
    db.close()  # teardown


def test_db(db):
    result = db.some_action()
    assert result == 42
