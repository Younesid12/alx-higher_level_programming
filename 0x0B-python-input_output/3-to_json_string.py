#!/usr/bin/python3
""" defines a function"""

import json

def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.loads(my_obj)
