#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """ defines a BaseGeometry class"""
    def area(self):
        """raises an Exception with the message area() is not complicated"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
