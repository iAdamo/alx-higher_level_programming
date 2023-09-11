#!/usr/bin/python3
"""0-lookup module: explains python inheritance
Function: lookup()

Test file for this module is located in ./tests/
Run (python3 -m doctest -v ./tests/0-lookup.txt | tail-2) to test
remove the pipeline to see full details
Author: Adam Sanusi Babatunde
"""


def lookup(obj):
    """lookup - function that returns the list of available attributes
    and methods of an object
    Args:
        obj: class
    """
    return dir(obj)
