#!/usr/bin/python3
"""This module contains:
add_integer - function that adds up two integers.

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/0-add_integer.txt) to test
"""


def add_integer(a, b=98):
    """add_integer - adds 2 integers

    Args:
        a: positional argument a (must be an integer)
        b: keyword argumrnt b (must be an integer)

    Return:
        sum of two integers or the keyword value if one arg is given
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a + b)
