#!/usr/bin/python3
number = 97
while(number < 123):
    if 113 == number or 101 == number:
        number += 1
        continue
    print("{:s}".format(chr(number)), end='')
    number += 1
