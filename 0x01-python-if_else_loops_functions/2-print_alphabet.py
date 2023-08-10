#!/usr/bin/python3
""" A program that prints the ASCII alphabet, in lowercase,
not followed by a new line."""
for a in range(97, 123):
    print("{:c}".format(a), end='')
