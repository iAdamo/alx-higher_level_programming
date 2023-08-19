#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ function that deletes keys with a specific value in a dictionary.

        Args:
        a_dictionary: a dictionary
        value: searched value

        Return:
        A new new dict
    """
    if len(a_dictionary) == 0:
        return a_dictionary
    b_dictionary = a_dictionary.copy()
    for key, val in b_dictionary.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
