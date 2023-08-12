#!/usr/bin/python3
""" Function that prints a string in uppercase followed by a new line """


def uppercase(str):
    for each_chr in str:
        deca = ord(each_chr)
        if deca in range(97, 123):
            deca -= 32
        print("{}".format(chr(deca)), end='')
    print("{}".format(""))
