#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """safe_print_list - prints x elements of a list.

    Args:
        my_list: contain any type (integer, string, etc.)
        x: epresents the number of elements to print

    Return:
        the real number of elements printed
    """
    try:
        for i in range(x):
            print(my_list[i], end='')
        print()
        return (x)
    except IndexError:
        print()
        return (i)
