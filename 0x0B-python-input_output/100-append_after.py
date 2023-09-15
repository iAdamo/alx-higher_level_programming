#!/usr/bin/python3
"""
100-append_after module
It supplies `append_after` function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Write a function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename: file to read and append into
        search_string: the search string to insert after
        new_string: new string to insert

    Return:
        None
    """
    # check if arguments are strings
    if filename == "" or search_string == "" or new_string == "":
        return

    # opening a file for append
    with open(filename, 'r', encoding='utf-8') as out:
        line_list = out.readlines()
        new_file = ""
    # loop through each content in line_list
        for each_line in line_list:
            new_file += each_line
            if search_string in each_line:
                new_file += new_string

    # open the file for writing and write the new_file into it
    with open(filename, 'w', encoding='utf-8') as out:
        out.write(new_file)
