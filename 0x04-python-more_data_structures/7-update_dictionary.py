#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    if key is None or value is None:
        return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
