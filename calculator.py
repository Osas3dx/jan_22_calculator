"""
A calculator library.
"""
import math

def add(*args):
    """
    add() Returns the sum of n-parameters.
    """
    return sum(args)


def divide(*args):
    """
    Returns the result of the division of n-parameters.
    """
    if not args:
        return math.nan
    if len(args) == 1:
        return 1

    args = list(args)
    answer = args.pop(0)

    for value in args:
        try:
            answer /= value
        except ZeroDivisionError:
            return math.nan

    return answer
