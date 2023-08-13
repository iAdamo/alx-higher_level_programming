#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit()

argc = len(argv) - 1
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] == '+':
    result = add(int(argv[1]), int(argv[3]))
elif argv[2] == '-':
    result = sub(int(argv[1]), int(argv[3]))
elif argv[2] == '*':
    result = mul(int(argv[1]), int(argv[3]))
elif argv[2] == '/':
    result = div(int(argv[1]), int(argv[3]))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

print("{:s} {:s} {:s} = {:d}".format(argv[1], argv[2], argv[3], result))
