#!/usr/bin/python3
if __name__ != "__main__":
    exit


def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position

        Args:
        my_list: list of elements
        idx: index
        element: element

        Return: a new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list.pop(idx)
    my_list.insert(idx, element)
    return my_list
