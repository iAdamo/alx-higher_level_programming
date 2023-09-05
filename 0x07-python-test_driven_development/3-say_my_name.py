#!/usr/bin/python3
"""function that prints My name is <first name> <last name>

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2) to test.
remove the pipeline to see full details"""


def say_my_name(first_name, last_name=""):
    """say_my_name - prints My name is <first name> <last name>

    Args:
        firstname: a string
        last_name: a string

    Return:
        Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    space = " "
    print(f"My name is {first_name}{space}{last_name}")
