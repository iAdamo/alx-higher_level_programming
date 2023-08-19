#!/usr/bin/python3
if __name__ != "__main__":
    exit


def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) == 0:
        return {}
    a_dictionary[key] = value
    return a_dictionary
