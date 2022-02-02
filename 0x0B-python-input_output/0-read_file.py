#!/usr/bin/python3

'''Task 00 - 0. Read file'''


def read_file(filename=""):
    '''function that reads a text file (UTF8)
    and prints it to stdout:'''
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")
