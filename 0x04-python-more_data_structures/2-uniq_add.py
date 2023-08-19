#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Write a function that adds all unique integers in a list
    (only once for each integer).

        Args:
        my_list: my list

        Return: addition of unique ints
    """
    if len(my_list) == 0:
        return 0
    return sum(set(my_list))
