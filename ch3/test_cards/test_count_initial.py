import cards

def test_empty():
    db = cards.CardsDB()
    count = db.count()
    db.close()
    assert count == 0

