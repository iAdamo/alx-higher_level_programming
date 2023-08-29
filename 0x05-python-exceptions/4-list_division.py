#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """list_division - function that divides element by element 2 lists.

    Args:
        my_list1: list 1
        my_list2: list 2
        list_length: list length

    Return:
    a new list (length = list_length) with all divisions
    """
    try:
        new_list = []
        for i in range(list_length):
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except IndexError:
                new_list.append(0)
                print("out of range")
    finally:
        return (new_list)
