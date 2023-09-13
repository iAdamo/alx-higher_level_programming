#!/usr/bin/python3
"""
7-add_item module
save_to_json_file function; 5-save_to_json_file
load_from_json_file function; 6-load_from_json_file
argv function; sys module
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


lists = []
if len(argv) == 1:
    save_to_json_file(lists, 'add_item.json')
    exit(1)
lists = load_from_json_file('add_item.json')
for i in range(1, len(argv)):
    lists.append(argv[i])
save_to_json_file(lists, 'add_item.json')
