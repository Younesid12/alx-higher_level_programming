#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Square class representation"""

    def __init__(self, size=0):
        """Initialization of attributes.

        Args:
            size (int): must be an integer
        """
        self.size = size

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
