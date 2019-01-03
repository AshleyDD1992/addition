import pytest
from addition import addition, subtract

def test_add_a_to_b():
    assert addition(2,2) == 4

def test_subtract_a_from_b():
    assert subtract(3,4) == 1