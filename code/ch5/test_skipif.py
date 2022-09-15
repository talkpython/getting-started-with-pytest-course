import cards
import pytest
from cards import Card
from packaging.version import parse


def test_packaging():
    v = parse(cards.__version__)
    print(f"{v.major=}, {v.minor=}, {v.micro=}")
    assert f"{v.major}.{v.minor}.{v.micro}" == cards.__version__


@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="sort not supported on version 1.x")
def test_sort():
    card_list = [Card("zzz"), Card("aaa")]
    s = sorted(card_list)
    assert s[0].summary == "aaa"
    assert s[1].summary == "zzz"


@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="less than not supported on version 1.x")
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2


def test_equality():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2
