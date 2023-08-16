#!/usr/bin/python3
if __name__ != "__main__":
    exit


def no_c(my_string):
    """ function that removes all characters c and C from a string

        Args:
        my_string: string

        Return:
        A new string without c and C in it
    """
    if 'c' not in my_string and 'C' not in my_string:
        return my_string
    for idx in range(len(my_string)):
        if my_string[idx] == 'c' or my_string[idx] == 'C':
            new_string = my_string[:idx] + my_string[idx + 1:]
            return no_c(new_string)
