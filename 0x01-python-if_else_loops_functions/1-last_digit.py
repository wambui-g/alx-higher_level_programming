#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)

if number < 0:
    num = number * -1
    num = num % 10
    num = num * -1
else:
    num = number % 10
print(f"Last digit of {number}", end= ' ')

if num > 5:
    print(f"is {num} and is greater than 5")
elif num == 0:
    print(f"is {num} and is 0")
elif num < 6 and num != 0:
    print(f"is {num} and is less than 6 and not 0")
