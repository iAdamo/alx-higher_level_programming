#!/usr/bin/python3
if __name__ != "__main__":
    exit


def new_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position

        Args:
        my_list: list of elements
        idx: index
        element: element

        Return: a new list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    myListCopy = my_list.copy()
    myListCopy.pop(idx)
    myListCopy.insert(idx, element)
    return myListCopy
