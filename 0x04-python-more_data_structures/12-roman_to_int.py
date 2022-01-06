#!/usr/bin/python3
def roman_to_int(roman_string):
    value = 0
    if not (isinstance(roman_string, str)):
        return (0)
    for i in range(len(roman_string)):
        if (roman_string[i] == 'I'):
            value += 1
        if (roman_string[i] == 'V'):
            if (roman_string[i - 1] == 'I' and i != 0):
                value -= 2
            value += 5
        if (roman_string[i] == 'X'):
            if (roman_string[i - 1] == 'I' and i != 0):
                value -= 2
            value += 10
        if (roman_string[i] == 'L'):
            if (roman_string[i - 1] == 'X' and i != 0):
                value -= 20
            value += 50
        if (roman_string[i] == 'C'):
            if (roman_string[i - 1] == 'X' and i != 0):
                value -= 20
            value += 100
        if (roman_string[i] == 'D'):
            if (roman_string[i - 1] == 'C' and i != 0):
                value -= 200
            value += 500
        if (roman_string[i] == 'M'):
            if (roman_string[i - 1] == 'C' and i != 0):
                value -= 200
            value += 1000
    return (value)
