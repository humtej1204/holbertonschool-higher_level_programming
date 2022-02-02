#!/usr/bin/python3

'''Task 07 - 7. Load, add, save'''


import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    f = load(file)
except:
    f = []

argc = len(sys.argv)
for i in range(1, argc):
    f.append(sys.argv[i])

save(f, file)
