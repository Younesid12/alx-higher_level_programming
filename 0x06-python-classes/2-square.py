#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Square class represention"""

    def __init__(self, size=0):
        """Direct Inatialization of attributes of this Class.
        Args:
            size (int): private instance attribute, should be an int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
