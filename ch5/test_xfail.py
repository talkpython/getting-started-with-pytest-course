import pytest
from cards import Card
from packaging.version import parse 
import cards

@pytest.mark.xfail(
    parse(cards.__version__).major < 2,
    reason="less than not supported on version 1.x")
def test_less_than():
    c1 = Card("a task")
    c2 = Card("b task")
    assert c1 < c2

@pytest.mark.xfail(reason="XPASS demo")
def test_xpass():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2

@pytest.mark.xfail(reason="XPASS demo", strict=True)
def test_xpass_strict():
    c1 = Card("a task")
    c2 = Card("a task")
    assert c1 == c2