#!/usr/bin/python3
if __name__ != "__main__":
    exit


def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list, in reverse order

        Args:
            my_list: list of integers

        Return:
            None
    """
    if type(my_list) is list:
        my_list.reverse()
        for each_int in my_list:
            print("{:d}".format(each_int))
