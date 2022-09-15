import cards
import pytest


@pytest.fixture(scope="session")
def cards_db_session(tmp_path_factory):
    """
    Returns a connection to the cards db
    """
    # setup
    db_path = tmp_path_factory.mktemp("cards_db_temp")
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
