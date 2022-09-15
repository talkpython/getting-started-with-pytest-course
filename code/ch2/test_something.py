def test_pass():
    a = (1, 2, 3)
    assert a == (1, 2, 3)


def test_fail():
    a = (1, 2, 3)
    assert a == (3, 2, 1)


def test_fail2():
    a = (1, 2, 3)
    assert a == (1, 2, 3, 4)
