#!/usr/bin/python3
""" defines a function"""

import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as n:
        data = json.load(n)
    return data
