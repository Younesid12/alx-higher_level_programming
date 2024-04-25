#!/usr/bin/python3
"""defines a square class that inherits from rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class that inherits from Rectangle superclass"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialized the attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ should return [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """returns the size"""
        return self.width

    @size.setter
    def size(self, size):
        """sets the size"""
        self.width = size

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
