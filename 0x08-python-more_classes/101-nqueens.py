#!/usr/bin/python3
if __name__ != '__main__':
    exit
"""This a program that solves the N queens problem
Author: Adam Sanusi Babatunde

Program must be run as the main program, if not it exits (not a module)
"""

import sys
"""From 'sys' module importing:
    argv: command line arguments
    stderr: standard error handling
"""

if len(sys.argv) != 2:
    print('Usage: nqueens N', file=sys.stderr)
    exit(1)

N = eval(sys.argv[1])

if not isinstance(N, int):
    print('N must be a number', file=sys.stderr)
    exit(1)
if N < 4:
    print('N must be at least 4', file=sys.stderr)
    exit(1)
