import pytest
from cards import Card

# function parametrization

@pytest.mark.parametrize(
    "start_state", ["todo", "in prog", "done"])
def test_finish_func(cards_db, start_state):
    c = Card("something", state=start_state)
    i = cards_db.add_card(c)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"


# fixture parametrization

@pytest.fixture(
    params=["todo", "in prog", "done"]
    )
def start_state(request):
    return request.param

def test_finish(cards_db, start_state):
    c = Card("something", state=start_state)
    i = cards_db.add_card(c)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"