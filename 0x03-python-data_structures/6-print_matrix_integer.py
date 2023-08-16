#!/usr/bin/python3
if __name__ != "__main__":
    exit


def print_matrix_integer(matrix=[[]]):
    """ function that prints a matrix of integers.

        Args:
        matrix: list in matrix

        Return:
        None
    """
    if matrix == [[]]:
        print()
    else:
        n = len(matrix)
        for each_item in matrix:
            if isinstance(each_item, list):
                print_matrix_integer(each_item)
            else:
                if n != 1:
                    print("{} ".format(each_item), end='')
                else:
                    print("{}".format(each_item))
                n -= 1
