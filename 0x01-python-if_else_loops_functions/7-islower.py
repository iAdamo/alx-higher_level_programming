#!/usr/bin/python3
"""function that checks for lowercase character."""


def islower(c):
    for deca in range(97, 123):
        if ord(c) == deca:
            return (True)
        else:
            continue
    return (False)
