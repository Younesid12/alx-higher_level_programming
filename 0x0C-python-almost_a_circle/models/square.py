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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
