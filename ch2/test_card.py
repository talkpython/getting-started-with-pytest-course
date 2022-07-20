from cards import Card

def test_field_access():
    c = Card("something", "brian", "todo", 123)
    assert c.summary == "something"
    assert c.owner == "brian"
    assert c.state == "todo"
    assert c.id == 123

def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None


def test_equality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 123)
    assert c1 == c2

def test_equality_with_diff_ids():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 4567)
    assert c1 == c2

def test_inequality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("completely different", "okken", "done", 123)
    assert c1 != c2

def test_from_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2_dict = { "summary": "something",
                "owner": "brian",
                "state": "todo",
                "id": 123 }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2

def test_to_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2 = c1.to_dict()
    c2_expected = { "summary": "something",
                    "owner": "brian",
                    "state": "todo",
                    "id": 123 }
    assert c2 == c2_expected
