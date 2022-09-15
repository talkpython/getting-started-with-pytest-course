def test_empty(cards_db):
    # GIVEN an empty database
    # WHEN count() is called
    count = cards_db.count()
    # THEN count returns 0
    assert count == 0
