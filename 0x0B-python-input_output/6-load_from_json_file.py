#!/usr/bin/python3
"""
6-load_from_json_file module
load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename: serialized file to load from

    Return:
        a deserialized output
    """
    with open(filename, 'r', encoding='utf-8') as out:
        return (json.load(out))
