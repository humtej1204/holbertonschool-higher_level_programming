#!/usr/bin/python3

'''Task 07 - 7. Load, add, save'''


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    f = load_from_json_file("add_item.json")
except:
    f = []

argc = len(sys.argv)
for i in range(1, argc):
    f.append(sys.argv[i])

save_to_json_file(f, "add_item.json")
