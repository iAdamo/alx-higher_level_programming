#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None
    return [[each_int ** 2 for each_int in each_item] for each_item in matrix]
