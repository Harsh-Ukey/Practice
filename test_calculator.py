import pytest
from calculator import add, subtract, multiply

def test_add():
    assert add(10, 4) == 14
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(9, -1) == 10

def test_multiply():
    assert multiply(10, 4) == 40
    assert multiply(9, 2) == 18