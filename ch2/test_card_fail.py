from cards import Card

def test_equality_fail():
    c1 = Card("something", "brian")
    c2 = Card("foo", "okken")
    assert c1 == c2

if __name__ == '__main__':
    test_equality_fail()