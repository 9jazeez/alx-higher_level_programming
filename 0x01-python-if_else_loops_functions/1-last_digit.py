#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    c = number % -10
else:
    c = number % 10

if c == 0:
    print("Last digit of {} is {} and is zero".format(number, c))
else:
    print("Last digit of {} is {} and is {} ".format(number, c,\
        "less than 6 and not 0 " if c < 6 else " greater than 5"))

