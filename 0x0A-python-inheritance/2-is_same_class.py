#!/usr/bin/python3
"""defines a is_same_class function"""



def is_same_class(obj, a_class):
    """ returns true if the object is exactly an instance of the specified class
    otherwise false"""
    if type(obj) == a_class:
        return True
    return False
