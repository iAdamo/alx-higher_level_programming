#!/usr/bin/python3
if __name__ != "__main__":
    exit


def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None
    result = []
    for each_item in matrix:
        squares = map(lambda x: x ** 2, each_item)
        result.append(list(squares))
    return result
