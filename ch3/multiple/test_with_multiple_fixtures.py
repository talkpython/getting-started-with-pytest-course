import pytest

@pytest.fixture(scope="session")
def foo():
    return "FOO"

@pytest.fixture(scope="module")
def bar(foo):
    return "BAR"

@pytest.fixture()
def baz(foo, bar):
    return "BAZ"

def test_muli(foo, bar, baz):
    print(f"{foo=}")
    print(f"{bar=}")
    print(f"{baz=}")