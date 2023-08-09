#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} as is greater than 5")
elif lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
else:
    print(f"Last digit of {number} is {lastDigit} as is less than 6 and not 0")
