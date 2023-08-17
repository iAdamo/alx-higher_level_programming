#!/usr/bin/python3
if __name__ != "__main__":
    exit


def delete_at(my_list=[], idx=0):
    """  function that deletes the item at a specific position in a list

        Args:
        my_list: list of integers
        idx: index position to delete

        Return:
        a new list

    """
    new_list = []
    if len(my_list) == 0:
        return None
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    del my_list[idx]
    new_list = my_list.copy()
    return (new_list)
