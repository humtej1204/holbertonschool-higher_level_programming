#!/usr/bin/python3
digit1 = 0
digit2 = 1
while digit1 <= 8:
    while digit2 <= 9:
        if digit1 != digit2:
            print("{:d}".format(digit1), end='')
            if digit1 != 8:
                print("{:d}, ".format(digit2), end='')
            else:
                print("{:d}".format(digit2))
        digit2 += 1
    digit2 = digit1 + 1
    digit1 = digit1 + 1
