#!/usr/bin/python3
"""print whether the number stored in the variable number is
positive or negative."""
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negative")
