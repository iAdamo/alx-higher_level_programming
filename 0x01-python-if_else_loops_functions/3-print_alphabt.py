#!/usr/bin/python3
""" A program that prints the ASCII alphabet, in lowercase,
not followed by a new line."""
for a in range(97, 123):
    if a == 101 or a == 113:
        continue
    print("{:c}".format(a), end='')
