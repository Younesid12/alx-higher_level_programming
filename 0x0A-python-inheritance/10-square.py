#!/usr/bin/python3
"""defines a class a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class definition"""
    def __init__(self, size):
        """initializes size"""
        try:
            super().__init__(size, size)
        except ValueError:
            raise ValueError("size must be greater than 0")
        except TypeError:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
