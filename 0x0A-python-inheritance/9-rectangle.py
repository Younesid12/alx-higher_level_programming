#!/usr/bin/python3
""" Defines a Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initializes instance attributes"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """finds the area"""
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__height}/{self.__width}"
