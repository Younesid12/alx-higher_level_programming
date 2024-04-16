#!/usr/bin/python3
""" Defines a Rectangle class"""

from base_geometry import BaseGeometry
class Rectangle(n):
    """Rectangle class"""
    def __init__(self, width, height):
        """initializes instance attributes"""
        n.integer_validator("height", height)
        n.integer_validator("width", width)
        self.__width = width
        self.__height = height
