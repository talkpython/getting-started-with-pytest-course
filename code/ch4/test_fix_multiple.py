import pytest
from cards import Card

@pytest.fixture(params=["todo", "in prog", "done"])
def start_state(request):
    return request.param

@pytest.fixture(params=["one", "two"])
def start_summary(request):
    return request.param

def test_finish(cards_db, start_summary, start_state):
  c = Card(summary=start_summary, state=start_state)
  i = cards_db.add_card(c)
  cards_db.finish(i)
  final_state = cards_db.get_card(i).state
  assert final_state == "done"