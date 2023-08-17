#!/usr/bin/python3
if __name__ != "__main__":
    exit


def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = []
    for each_int in my_list:
        if each_int % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
