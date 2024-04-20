#!/usr/bin/python3
"""defines a a function"""


def append_write(filename="", text=""):
    """appends a string at the end of a file and returns number 0of char added"""
    with open(filename, 'a', encoding='utf-8') as n:
        num_bytes = n.write(text)
    return num_bytes
