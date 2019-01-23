"""
Tests the add() function of the calculator.
"""
from calculator import add


def test_two_plus_two():
    """
    If given 2 and 2 as parameters, 4 should
    be returned.
    """
    assert add(2, 2) == 4
