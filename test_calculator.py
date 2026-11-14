import pytest
from calculator import add, multiply, sub, div

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(4, 5) == 20

def test_sub():
    assert sub(10, 4) == 6

def test_div():
    assert div(10, 4) == 2.5

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
