#!/usr/bin/python3
if __name__ != "__main__":
    exit


def simple_delete(a_dictionary, key=""):
    if len(a_dictionary) == 0:
        return {}
    if len(key) == 0 or key not in a_dictionary:
        return a_dictionary

    del a_dictionary[key]
    return a_dictionary
