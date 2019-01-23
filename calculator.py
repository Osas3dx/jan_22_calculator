"""
A calculator library.
"""
def add(*args):
    answer = 0
    for value in args:
        answer += value
    return answer
