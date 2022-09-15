import pathlib
import pytest
from tempfile import TemporaryDirectory
import cards

@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        # setup
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)

        yield db 

        # teardown
        db.close()



def test_empty(cards_db):
    count = cards_db.count()
    assert count == 0


def test_one_item(cards_db):
    # GIVEN a database with 1 item
    cards_db.add_card(cards.Card("something"))
    # WHEN count() is called
    count = cards_db.count()
    # THEN count returns 1
    assert count == 1