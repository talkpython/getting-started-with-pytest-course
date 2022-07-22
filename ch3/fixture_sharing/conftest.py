import pathlib
import pytest
from tempfile import TemporaryDirectory
import cards

@pytest.fixture(scope="session")
def cards_db_session():
    """
    Returns a connection to the cards db
    """
    with TemporaryDirectory() as db_dir:
        # setup
        db_path = pathlib.Path(db_dir)
        db = cards.CardsDB(db_path)
        yield db 
        # teardown
        db.close()

@pytest.fixture(scope="function")
def cards_db(cards_db_session):
    """
    Returns a connection an empty cards db
    """
    cards_db_session.delete_all()
    return cards_db_session