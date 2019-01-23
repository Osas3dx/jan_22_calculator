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


def test_three_and_three():
    """
    If given 3 and 3, 6 should be returned.
    """
    assert add(3, 3) == 6


def test_no_parameters():
    """
    If no parameters are provided, return 0.
    """
    assert add() == 0
