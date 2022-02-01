#!/usr/bin/python3

'''Task 03 - 3. To JSON string'''


import json


def to_json_string(my_obj):
    '''function that returns the JSON representation
    of an object (string)'''
    s = json.dumps(my_obj)
    return s
