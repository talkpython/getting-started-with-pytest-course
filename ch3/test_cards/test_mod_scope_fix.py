from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

@pytest.fixture(scope='module')
def cards_db_module():
    # setup
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        # teardown
        db.close()

@pytest.fixture(scope='function')
def cards_db(cards_db_module):
    db = cards_db_module
    db.delete_all()
    return db


def test_non_empty(cards_db):
    # GIVEN a database with 2 cards
    cards_db.delete_all() # start with 0
    c1 = cards.Card("do something", "brian")
    c2 = cards.Card("something else", "brian")
    cards_db.add_card(c1)
    cards_db.add_card(c2)
    # WHEN count() is called
    count = cards_db.count()
    # THEN count is 2
    assert cards_db.count() == 2


def test_empty(cards_db):
    # GIVEN an empty database
    cards_db.delete_all() 
    # WHEN count() is called
    count = cards_db.count()
    # THEN count is 0
    assert count == 0
