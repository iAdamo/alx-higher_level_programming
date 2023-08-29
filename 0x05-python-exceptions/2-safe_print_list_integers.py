#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """safe_print_list_integers -  prints the first x elements of a list
    and only integers.

    Args:
        my_list: can contain any type (integer, string, etc.)
        x:  number of elements to access in my_list

    Return:
        the real number of integers printed
    """
    real = x
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (TypeError, ValueError):
            real -= 1
    print()
    return (real)
