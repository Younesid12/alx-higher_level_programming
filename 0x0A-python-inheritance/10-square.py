#!/usr/bin/python3
"""defines a class square"""

Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """initializes size"""
        supper().__init__(size, size)
        self.__size = size
