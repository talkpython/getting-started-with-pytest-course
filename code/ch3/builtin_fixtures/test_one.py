import cards

def test_one_item(cards_db):
    # GIVEN a database with 1 item
    cards_db.add_card(cards.Card("something"))
    # WHEN count() is called
    count = cards_db.count()
    # THEN count returns 1
    assert count == 1