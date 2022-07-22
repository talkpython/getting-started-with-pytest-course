import pytest

@pytest.fixture(params = [1, 2, 3])
def foo(request):
    return request.param  
    
def test_foo(foo): 
    assert foo in (1, 2, 3)

@pytest.fixture(params = [("foo", 1), ("bar", 2)])
def baz(request):
    return request.param  
    
def test_baz(baz): 
    thing1, thing2 = baz
    assert thing1 in ("foo", "bar")
    assert thing2 in (1, 2)
