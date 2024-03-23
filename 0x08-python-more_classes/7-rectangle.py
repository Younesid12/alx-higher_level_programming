#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle():
    """Defines a rectangle class."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes a new instance"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints the rectanlge with the character #, if width or heigth is 0,
        returns an empty str"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            n = ""
            for i in range(self.__height):
                if i is not range(self.__height - 1:
                        n += f"{self.print_symbol * self.__width}\n"
                else:
                    n += f"{self.print_symbol * self.__width"}
            return n

    def __repr__(self):
        """returns the strig representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """invoked when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """ retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets a value to width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height attr"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of a treangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)
