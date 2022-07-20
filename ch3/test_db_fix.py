import pytest
from some_db import DB

@pytest.fixture()
def db():
    db = DB() 
    yield db
    db.close() 

def test_db(db):
    result = db.some_action()
    assert result == 42