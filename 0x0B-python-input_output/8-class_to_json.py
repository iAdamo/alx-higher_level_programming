#!/usr/bin/python3
"""
This it the 8-class_to_json module
It supplies class_to_json function
"""
import json


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: an instance of a Class

        All attributes of the obj Class are serializable:
        list, dictionary, string, integer and boolean

    Return:
        returns the dictionary description with simple data structure
    """
    return vars(obj)
