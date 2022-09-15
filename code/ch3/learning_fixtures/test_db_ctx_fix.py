from contextlib import closing

import pytest

from some_db import DB


@pytest.fixture()
def db():
    with closing(DB()) as db:
        yield db


def test_db(db):
    result = db.some_action()
    assert result == 42
