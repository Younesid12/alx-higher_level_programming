#!/usr/bin/python3
"""defines a function"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    json.load(my_object, filename)
