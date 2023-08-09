#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastUnit = abs(number) % 10
if number < 0:
    lastUnit *= -1
if lastUnit > 5:
    print(f"Last digit of {number} is {lastUnit} and is greater than 5")
elif lastUnit == 0:
    print(f"Last digit of {number} is {lastUnit} and is 0")
else:
    print(f"Last digit of {number} is {lastUnit} and is less than 6 and not 0")
