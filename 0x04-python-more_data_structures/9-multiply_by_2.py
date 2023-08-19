#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0:
        return ({})
    new_dict = dict()
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
