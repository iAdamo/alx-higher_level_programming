#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file

Usage:
    add_item arg1 arg2 ...

If the file doesn’t exist, it should be created
load_from_json_file: loads the file for deserializing
command line args are made into list
load_from_json_file: list are saved back into the file by serializing them
"""
from sys import argv
from os import path.exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

lists = []
if len(argv) > 1:
    if not path.exists('add_item.json'):
        save_to_json_file(lists, 'add_item.json')

    lists = load_from_json_file('add_item.json')

    for i in range(1, len(argv)):
        lists.append(argv[i])

    save_to_json_file(lists, 'add_item.json')
else:
    save_to_json_file(lists, 'add_item.json')
