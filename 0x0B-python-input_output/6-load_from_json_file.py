#!/usr/bin/python3

'''Task 06 - 6. Create object from a JSON file'''


import json


def load_from_json_file(filename):
    '''function that creates an Object from a JSON file'''
    with open(filename, mode='r') as f:
        s = json.loads(f.read())
        return s
