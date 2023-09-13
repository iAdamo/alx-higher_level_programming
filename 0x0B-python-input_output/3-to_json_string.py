#!/usr/bin/python3
"""
3-to_json_string module
to_json_string function
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
