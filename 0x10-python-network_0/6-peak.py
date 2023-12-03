#!/usr/bin/python3
"""Contains a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        lis_of_integers(list): list of integers

    Return:
        (Int)The peak
    """
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for num in list_of_integers:
        if num > peak:
            peak = num
    return peak
