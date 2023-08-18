#!/usr/bin/python3
if __name__ != "__main__":
    exit


def uniq_add(my_list=[]):
    """Write a function that adds all unique integers in a list
    (only once for each integer).

        Args:
        my_list: my list

        Return: addition of unique ints
    """
    if len(my_list) == 0:
        return 0
    my_list = list(set(my_list))
    add = 0
    for each_int in my_list:
        add += each_int
    return (add)
