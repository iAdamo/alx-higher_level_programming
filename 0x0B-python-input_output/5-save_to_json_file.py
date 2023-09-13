#!/usr/bin/python3
"""
5-save_to_json_file module
save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation

    Args:
        my_obj: my object to serialize
        filename: file to write
    """
    with open(filename, 'w', encoding='utf-8') as out:
        json.dump(my_obj, out)
