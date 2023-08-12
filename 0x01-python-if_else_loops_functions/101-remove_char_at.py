#!/usr/bin/python3

def remove_char_at(str, n):
    if n > len(str) or n < 0:
        print(str)
    else:
        new_str = []
        for each_char in str:
            new_str.append(each_char)
        new_str.pop(n)
        for each_char in new_str:
            print("{}".format(each_char), end='')
        print()
