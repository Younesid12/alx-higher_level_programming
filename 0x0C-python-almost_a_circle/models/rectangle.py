#!/usr/bin/python3
"""defines a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the instance's attributes of this class"""
        super.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @propery
    def width(self):
        """gets the width value"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets a value to the width attribute"""
        self.__width = value

    @property
    def height(self):
        """returns the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the new value to the height attribute"""
        self.__height = height

    @property
    def x(self):
        """returns the value of x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """ assigns x a new value"""
        self.__x = x

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y attribute a new value"""
        self.__y = y

