#!/usr/bin/python3
"""A program that prints all possible different combinations of two digits."""
for tenth in range(0, 10):
    for unit in range(tenth + 1, 10):
        if tenth != 8:
            print("{}{}, ".format(tenth, unit), end='')
        else:
            print("89")
