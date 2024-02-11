#!/usr/bin/python3

"""Defines a square Class"""


class Square:
    """Square class representation"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of a new instance's attributes.

        Args:
            size (int): size of the square
            position (tuple): must be a tuple of two positive integers
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrives the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """retrieves the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        for n in value:
            if n < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
            return
        else:
            for n in range(1, self.area() + 1):
                print("{}".format("#"), end='')
                if n % self.__size == 0:
                    print()
