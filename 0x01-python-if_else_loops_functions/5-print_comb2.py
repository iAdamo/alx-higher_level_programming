#!/usr/bin/python3
""" a program that prints numbers from 0 to 99 """
for num in range(0, 100):
    if num != 99:
        print("{:02d}, ".format(num), end='')
    else:
        print("99")
