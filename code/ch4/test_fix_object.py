import pytest
from cards import Card


@pytest.fixture(params=[
    Card("one", state="todo"),
    Card("two", state="in prog"),
    Card("three", state="done")],
    ids=lambda x: x.state)
def start_card(request):
    return request.param


def test_finish(cards_db, start_card):
    i = cards_db.add_card(start_card)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"
