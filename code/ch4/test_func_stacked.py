import pytest
from cards import Card


@pytest.mark.parametrize("start_state", ["todo", "in prog", "done"])
@pytest.mark.parametrize("start_summary", ["one", "two"])
def test_finish(cards_db, start_summary, start_state):
    c = Card(summary=start_summary, state=start_state)
    i = cards_db.add_card(c)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"
