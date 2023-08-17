#!/usr/bin/python3
if __name__ != "__main__":
    exit


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    sorted_list = sorted(my_list)
    max_num = sorted_list[len(sorted_list) - 1]
    return (max_num)
