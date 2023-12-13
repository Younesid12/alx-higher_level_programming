#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
find_digit = str(number)
digit = 0
for char in find_digit:
    if char == '-':
        continue
    digit = int(char)
if digit > 5:
    print(f"Last digit of {find_digit} is {digit} and is greater than 5")
elif digit < 6 and digit != 0:
    print(f"Last digit of {find_digit} is {digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {find_digit} is {digit} and is 0")
