import pathlib
from tempfile import TemporaryDirectory

import cards
import pytest


@pytest.fixture(scope="module")
def cards_db_module():
    with TemporaryDirectory() as db_dir:
        # setup
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        # teardown
        db.close()


@pytest.fixture(scope="function")
def cards_db(cards_db_module):
    cards_db_module.delete_all()
    return cards_db_module


def test_one_item(cards_db):
    # GIVEN a database with 1 item
    cards_db.add_card(cards.Card("something"))
    # WHEN count() is called
    count = cards_db.count()
    # THEN count returns 1
    assert count == 1


def test_empty(cards_db):
    # GIVEN an empty database
    # WHEN count() is called
    count = cards_db.count()
    # THEN count returns 0
    assert count == 0
