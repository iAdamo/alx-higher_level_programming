#!/usr/bin/python3
"""
This is the 12-pascal_triangle module
pascal_triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n: always an integer

    Return:
        an empty list if n <= 0
    """
    triangle = []
    for _ in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                pascal.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)
    return triangle
