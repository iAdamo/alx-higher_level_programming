#!/usr/bin/python3


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
        return []
    if search not in my_list:
        return my_list
    return ([item if item != search else replace for item in my_list])
