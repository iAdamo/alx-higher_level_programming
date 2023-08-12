#!/usr/bin/python3
"""function that prints the numbers from 1 to 100 separated by a space."""


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 != 0:
            print("Fizz ", end='')
        elif num % 5 == 0 and num % 3 != 0:
            print("Buzz ", end='')
        elif (num % 3 and num % 5) == 0:
            print("FizzBuzz ", end='')
        else:
            print(f"{num} ", end='')
