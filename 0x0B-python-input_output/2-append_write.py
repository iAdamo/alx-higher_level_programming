#!/usr/bin/python3
"""
2-append_write module
append_write function
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)

    Args:
        filename: file to be written into and appended to
        text: text to append

    Return:
        the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as out:
        return out.write(text)
