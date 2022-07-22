from cards import Card

# states are "todo", "in prog", "done"

def test_finish_todo(cards_db):
    c = Card("something", state="todo")
    i = cards_db.add_card(c)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"

def test_finish_in_prog(cards_db):
    c = Card("something", state="in prog")
    i = cards_db.add_card(c)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"

def test_finish_done(cards_db):
    c = Card("something", state="done")
    i = cards_db.add_card(c)
    cards_db.finish(i)
    final_state = cards_db.get_card(i).state
    assert final_state == "done"