#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
no = abs(number) % 10
if number < 0:
    no = -no
print("Last digit of {} is {} and is ".format(number, no), end="")
if no > 5:
    print("greater than 5")
elif no == 0:
    print("0")
else:
    print("less than 6 and is 0")
