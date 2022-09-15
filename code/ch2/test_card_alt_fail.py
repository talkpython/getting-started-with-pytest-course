import pytest
from cards import Card

def test_equality_fail():
    c1 = Card("something", "brian")
    c2 = Card("foo", "okken")
    if c1 != c2:
        pytest.fail("They are not equal")

def test_equality_fail_2():
    c1 = Card("something", "brian")
    c2 = Card("foo", "okken")
    if c1 != c2:
        raise Exception("They are not equal")

