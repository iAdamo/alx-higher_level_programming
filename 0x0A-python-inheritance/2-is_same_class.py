#!/usr/bin/python3
"""2-is_same_class module: python inheritance

Test file for this module is located in ./tests/
Run (python3 -m doctest -v ./tests/2-is_same_class.txt | tail -2) to test
Remove the pipeline to see full details
"""


def is_same_class(obj, a_class):
    """is_same_class - a function that returns True if the object is exactly
    an instance of the specified class

    Args:
        obj: unknown object
        a_class: class object
    """
    return isinstance(obj, a_class)
