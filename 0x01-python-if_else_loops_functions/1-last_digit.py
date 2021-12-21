#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = -number % 10
    n = -n
else:
    n = number % 10

if n > 5:
    str = "and is greater than 5"
elif n == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d} {:s}".format(number, n, str))
