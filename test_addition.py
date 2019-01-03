import pytest
from addition import addition

def test_add_a_to_b():
    assert addition(1,2) == 3
