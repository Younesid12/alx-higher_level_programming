#!/usr/bin/python3
""" Defines a Rectangle class"""


n = __import__("7-base_geometry.py").BaseGeometry
class Rectangle(n):
    """Rectangle class"""
    def __init__(self, width, height):
        """initializes instance attributes"""
        n.integer_validator("height", height)
        n.integer_validator("width", width)
        self.__width = width
        self.__height = height
