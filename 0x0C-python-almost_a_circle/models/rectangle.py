#!/usr/bin/python3
"""defines a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the instance's attributes of this class"""
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the width value"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets a value to the width attribute"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """returns the value of the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the new value to the height attribute"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """returns the value of x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """ assigns x a new value"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets y attribute a new value"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the rectangle instance with the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """returns a string"""
        return f"[Rectangle] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value
            return
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
