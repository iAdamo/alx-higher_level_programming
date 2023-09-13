#!/usr/bin/python3
"""0-read_file module: Input and Output
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
    Args:
        filename: file to read from
    """
    with open(filename, encoding='utf-8') as out:
        print(out.read(), end='')
