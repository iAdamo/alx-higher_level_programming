#!/usr/bin/python3
if __name__ != "__main__":
    exit


def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element by another
      in a new list.

        Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element

        Return:
        A new list
    """
    if len(my_list) == 0:
        return None
    if 2 not in my_list:
        return my_list
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
