#!/usr/bin/python3
if __name__ != "__main__":
    exit


def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None
    result = []
    for each_item in matrix:
        result.append([each_int ** 2 for each_int in each_item])
    return result
