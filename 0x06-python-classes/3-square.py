#!/usr/bin/python3
"""Defines a Square class."""

class Square:
    """Class representing a square>"""

    def __init__(self, size=0):
        """Inizialization of a new square.

        Args:
            size (int): must be an integer greater than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
