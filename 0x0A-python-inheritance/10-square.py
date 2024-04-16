#!/usr/bin/python3
"""defines a class square"""

Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """initializes size"""
        Rectangle.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area"""
        return self.__size ** 2

    def __str__(self):
        """prints a string repreentation of square objects"""
        return f"[Rectangle] {size}/{size}"
