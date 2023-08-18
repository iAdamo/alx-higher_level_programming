#!/usr/bin/python3
if __name__ != "__main__":
    exit


def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
