#!/usr/bin/python3

"""Defines a Square Class"""


class Square:
    """Square Class representation"""

    def __init__(self, size=0):
        """Initialization of Square attributes.

        Args:
        size (int): must be an integer, it represents the square size.
        """
        self.__size = size

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @self.setter
    def size(self, value):
        """sets the value to the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if size == 0:
            print("")
            return
        for n in range(self.area):
            print("{}".format("#"))
            if n % self.__size = 0:
                print()

