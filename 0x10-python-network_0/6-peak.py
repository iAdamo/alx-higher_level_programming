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
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
