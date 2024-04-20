#!/usr/bin/python3
"""script that adds all arguments to a Python list
and then save them to a file"""

import sys
import json
from 5-save_to_json_file import save_to_json_file
from  6-load_from_json_file.py import load_from_json_file
liSt = []
for i in range(1, len(args):
        liSt.append(args[i]
with open(add_item.json, 'w', encoding='utf-8') as n:
        json.dump(liSt, add_item.json)
