#!/usr/bin/python3
"""1-write_file module - Write to a file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename: file to write into
        text: text to be written
    Return: the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as out:
        return out.write(text)
