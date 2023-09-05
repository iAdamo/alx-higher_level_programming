#!/usr/bin/python3
"""Module to print a square

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/4-print_square.txt) to test
to remove the pipeline to see full details"""


def print_square(size):
    """print_square - prints a square with the character #

    Args:
        size: size length of the square

    Return:
        Nothing
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for _ in range(size):
        print('#' * size)
