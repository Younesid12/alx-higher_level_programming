#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle():
    """Defines the Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes Rectangle attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width attr getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width attr setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attr getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attr setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
