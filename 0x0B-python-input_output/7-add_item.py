#!/usr/bin/python3

'''Task 07 - 7. Load, add, save'''


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    loadFile = load_from_json_file("add_item.json")
except FileNotFoundError:
    loadFile = []

argc = len(sys.argv)
for a in range(1, argc):
    loadFile.append(sys.argv[a])

save_to_json_file(loadFile, "add_item.json")
