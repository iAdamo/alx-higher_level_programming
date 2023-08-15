#!/usr/bin/python3
if __name__ != "__main__":
    exit


def element_at(my_list, idx):
    """Function that retrieves an element from a list like in C.

    Args:
        my_list: list of integers
        idx: position index

    Retuns:
        Element at at position idx
    """
    if idx < 0 or len(my_list) <= idx:
        return None
    return my_list[idx]
