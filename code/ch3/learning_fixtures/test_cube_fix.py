import pytest


@pytest.fixture()
def num():
    return 42


def test_cube(num):
    cube = num ** 3
    expected = num * num * num
    assert cube == expected
