from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

@pytest.fixture()
def cards_db():
    # setup
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db
        # teardown
        db.close()

def test_empty(cards_db):
    # GIVEN an empty database
    # WHEN count() is called
    count = cards_db.count()
    # THEN count is 0
    assert count == 0

def test_non_empty(cards_db):
    # GIVEN a database with 2 cards
    c1 = cards.Card("do something", "brian")
    c2 = cards.Card("something else", "brian")
    cards_db.add_card(c1)
    cards_db.add_card(c2)
    # WHEN count() is called
    count = cards_db.count()
    # THEN count is 2
    assert count == 2

