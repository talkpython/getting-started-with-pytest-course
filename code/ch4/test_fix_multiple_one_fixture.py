import pytest
from cards import Card


def id_func(x):
    return f"{x[0]}-{x[1]}"


@pytest.fixture(params=[
    ("one", "todo"),
    ("two", "in prog"),
    ("three", "done")],
    ids=id_func)
def state_summary(request):
    return request.param


def test_finish(cards_db, state_summary):
    start_state, start_summary = state_summary
    c = Card(summary=start_summary, state=start_state)
    i = cards_db.add_card(c)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"
