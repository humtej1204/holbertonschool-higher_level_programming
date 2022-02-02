#!/usr/bin/python3

'''Task 07 - 7. Load, add, save'''


import sys
import os


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
list_json = []

if os.path.isfile(filename):
    list_json = load(filename)

for item in sys.argv[1:]:
    list_json.append(item)

save(list_json, filename)
