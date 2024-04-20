#!/usr/bin/python3
"""defines a function"""


def write_file(filename='', text=''):
    """ writes a text to a file"""
    with open(filename, 'w', encoding='utf-8') as n:
        num_character = n.write(text)
    return num_character
