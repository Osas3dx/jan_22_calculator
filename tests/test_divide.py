"""
Tests the divide() function from calculator
"""
import math
from calculator import divide


def test_without_parameters():
    """
    Given that no parameters are provided to the
    function, return an nan float.
    """
    assert divide() is math.nan


def test_four_divided_by_two():
    assert divide(4, 2) == 2


def test_three_divided_by_nothing():
    """
    Given that the value 3 is provided, but no
    other parameter is, expect 1.
    """
    assert divide(3) == 1


def test_four_number_division():
    assert divide(300, 10, 10, 10) == 3 / 10


def test_a_zero_division():
    assert divide(3, 0) is math.nan
