from cards import Card

def test_finish(cards_db):
    for c in [
        Card("one", state="todo"),
        Card("two", state="in prog"),
        Card("three", state="done")
    ]:
        i = cards_db.add_card(c)
        cards_db.finish(i)
        final_state = cards_db.get_card(i).state
        assert final_state == "done"
