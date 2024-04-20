#!/usr/bin/python3
"""script that adds all arguments to a Python list
and then save them to a file"""

import sys
import json
save_to_json_file = __import__ ('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

liSt = []
for i in range(1, len(argv):
        liSt.append(sys.argv[i]
with open(add_item.json, 'w', encoding='utf-8') as n:
        save_to_json_file(liSt, 'add_item.json')
print(load_from_json_file('add_item.json')
