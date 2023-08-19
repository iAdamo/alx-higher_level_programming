#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        exit

    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
