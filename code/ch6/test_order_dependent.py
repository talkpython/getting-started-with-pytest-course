x = 0

def test_one():
    global x
    x = 1
    assert x == 1

def test_still_one():
    assert x == 1

def test_three():
    global x
    x = 3
    assert x == 3

def test_still_three():
    assert x == 3
