import pathlib
from tempfile import TemporaryDirectory

import cards


def test_empty():
    # GIVEN an empty database
    with TemporaryDirectory() as db_dir:
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        # WHEN count() is called
        count = db.count()
        # teardown
        db.close()
        # THEN count returns 0
        assert count == 0


def test_one_item():
    # GIVEN a database with 1 item
    with TemporaryDirectory() as db_dir:
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        db.add_card(cards.Card("something"))
        # WHEN count() is called
        count = db.count()
        # teardown
        db.close()
        # THEN count returns 1
        assert count == 1
