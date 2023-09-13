#!/usr/bin/python3
"""
4-json_to_string module
from_json_string function
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: strings

    Return:
        an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
