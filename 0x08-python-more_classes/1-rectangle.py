#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle():
    """ defines a Rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes the new created instance of this class.
        
        Args:
            width (int): the width of the rectangle, 0 as default
            height (int): the height of the rectangle. 0 as a default value
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value to width attribute """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self)
        """ retrieves the value of height or the height in other words """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height a new value """
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
