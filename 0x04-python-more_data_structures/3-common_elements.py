#!/usr/bin/python3
if __name__ != "__main__":
    exit


def common_elements(set_1, set_2):
    """ function that returns a set of common elements in two sets.

        Args:
        set_1: first set
        set_2: second set

        Return:
        returns a set of common elements in two sets
    """
    if len(set_1) == 0 and len(set_2) == 0:
        return {}
    return (each_item for each_item in set_1 if each_item in set_2)
