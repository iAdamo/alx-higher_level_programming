#!/usr/bin/python3
"""3-is_kind_of_class module: python inheritance

Test file for this module is located in ./tests/
Run (python3 -m doctest -v ./tests/2-is_same_class.txt | tail -2) to test
Remove the pipeline to see full details
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False

    Args:
        obj: unknown object
        a_class: class object
    """
    return isinstance(obj, a_class)
