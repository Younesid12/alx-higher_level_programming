#!/usr/bin/python3
""" Defines a Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initializes instance attributes"""
        self..integer_validator("height", height)
        self..integer_validator("width", width)
        self.__width = width
        self.__height = height
