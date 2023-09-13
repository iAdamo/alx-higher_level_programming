#!/usr/bin/python3
"""101-add_attribute module - add attribute
"""


def add_attribute(obj=object, attr=str, value=str):
    """dynamically set a new attribute to a class"""
    if not isinstance(obj, object):
        raise TypeError("can't add new attribute")
    for att in dir(obj):
        if att[2:-2] is attr:
            raise TypeError("can't add new attribute")
    obj.attr = value
