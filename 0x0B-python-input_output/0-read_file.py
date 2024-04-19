#!/usr/bin/python3
""" defines a function that reads a file"""


def read_file(filename=""):
    """Reads a file"""
    with open(filename, encoding='utf-8') as n:
        content = n.read()
    print(content)
