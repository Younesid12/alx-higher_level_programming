#!/usr/bin/python3
"""defines a class a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class definition"""
    def __init__(self, size):
        """initializes size"""
        supper().__init__(size, size)
        self.__size = size
