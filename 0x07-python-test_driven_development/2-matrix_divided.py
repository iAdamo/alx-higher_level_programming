#!/usr/bin/python3
"""function that divides all elements of a matrix

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/2-matrix_divided.txt) to test
"""


def matrix_divided(matrix, div):
    """matrix_divided -  divides all elements of a matrix

    Args:
        matrix: a list of lists of integers or floats
        div: number (integer or float)

    Return:
        a new matrix
    """

    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        for each_int in matrix[i]:
            if not isinstance(each_int, (int, float)):
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
        if len(matrix) != i + 1 and len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(_int / div, 2) for _int in _item] for _item in matrix]
