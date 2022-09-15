from cards import Card

def test_sort():
    card_list = [Card("zzz"), Card("aaa")]
    s = sorted(card_list)
    assert s[0].summary == "aaa"
    assert s[1].summary == "zzz"

def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2

def test_equality():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2
