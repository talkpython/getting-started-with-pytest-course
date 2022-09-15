"""
Recommended test structure pattern

    Arrange, Act, Assert
    -or-
    Given, When, Then
"""
from cards import Card

def test_to_dict():
    # GIVEN a card with know value
    c1 = Card("something", "brian", "todo", 123)

    # WHEN we call to_dict()
    c2 = c1.to_dict()

    # THEN we get the expected dictionary
    c2_expected = { "summary": "something",
                    "owner": "brian",
                    "state": "todo",
                    "id": 123 }
    assert c2 == c2_expected