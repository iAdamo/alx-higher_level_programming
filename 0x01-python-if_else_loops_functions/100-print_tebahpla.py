#!/usr/bin/python3
""" A program that prints the ASCII alphabet, in reverse order
alternating lowercase and uppercase, not followed by newline"""
for alpha in range(122, 96, -1):
    if alpha % 2:
        alpha -= 32
    print("{}".format(chr(alpha)), end='')
