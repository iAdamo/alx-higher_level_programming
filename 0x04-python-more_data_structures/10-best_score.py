#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    my_value = sorted(a_dictionary.values())
    idx = len(my_value) - 1
    biggest_value = my_value[idx]
    for key, value in a_dictionary.items():
        if value == biggest_value:
            return key
