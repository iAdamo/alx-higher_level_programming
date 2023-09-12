#!/usr/bin/python3
"""inherits_from module: python inheritance

Test file for this module is located in ./tests/
Run (python3 -m doctest -v ./tests/2-is_same_class.txt | tail -2) to test
Remove the pipeline to see full details
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of, or if the object is an
    instance of a class that inherited (directly or indirectly) from,
    the specified class; otherwise False

    Args:
        obj: unknown object (use type() to check for object type)
        a_class: class object
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
