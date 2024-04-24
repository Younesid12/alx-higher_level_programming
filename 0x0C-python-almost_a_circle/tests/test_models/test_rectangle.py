#!/usr/bin/python3
"""defines a unittest for the class rectangle that inherits
from Base class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests the Rectangle's code implementation"""
    def test_id_initialization(self):
        """tests initialization of id varibale that
        is defined in the super class"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_other_initializations(self):
        """checks the initialization of other variables
        width and height and x and y and checking if the
        getter methods work as expected"""
        n = Rectangle(10, 2, 3, 5, 12)
        self.assertEqual(n.height(), 2)
        self.assertEqual(n.width(), 10)
        self.assertEqual(n.x, 3)
        self.assertEqual(n.y, 5)

    def test_setter_methods(self):
        n = Rectangle(1, 2, 3, 4, 5)
        n.height(4)
        self.assertEqual(n.height(), 4)
        n.width(3)
        self.assertEqual(n.width(3))
        n.x(12)
        self.assertEqual(n.x(), 12)
        n.y(9)
        self.assertEqual(n.y(), 9)

    def test_typeError(self):
        """tests if TypeError is raised when the input passed
        is not an integer, this has to do with fist fourth parameters only"""
        with self.assertRaises(TypeError) as context:
            Rectangle(10, '2')
        raised_exception = context.exception
        self.assertEqual(str(raised_exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            Rectangle('3', 2)
        raised_exception = context.exception
        self.assertEqual(str(raised_exception), "width must be an integer")
        with self.assertEqual(TypeError) as context:
            Rectangle(10, 3, 'hello')
        raised_exception = context.exception
        self.assertEqual(str(raised_exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            Rectangle(10, 3, 4, 'nice')
        raised_context = context.exception
        self.assertEqual(str(raised_exception), "y must be an integer")

    def test_first_valueError(self):
        """tests if a ValueError exception is raised when
        a value under 0 is passed to either height or width
        variables and checks if the expected message is
        accompanied with the exception"""
        with self.assertRaises(ValueError) as n:
            Rectangle(-1, 2)
        excep = n.exception
        self.assertEqual(str(excep), "width must be > 0")
        with self.assertRaises(ValueError) as n:
            Rectangle(1, -8)
        excep = n.context
        self.assertEqual(str(excep), "height must be > 0")

    def test_x_y_valueError(self):
        """tests if a ValueError is raised with a message
        when a a negative number is passed as an argument for
        x and y"""
        with self.assertRaises(ValueError) as n:
            Rectangle(10, 2, -1):
        excep = n.context
        self.assertEqual(str(excep), "x must be >= 0")
        with self.assetRaises(ValueError) as n:
            Rectangle(1, 2, 3, -2)
        excep = n.context
        self.assertEqual(str(excep), "y must be >= 0")

    def test_setter(self):
    """tests if TypeError is raised when setting the first
    fourth variables(parameters) using setter methods
    this has to do with the first fourth parameters only"""
    with self.assertRaises(TypeError) as context:
        self.height('hello')
    raised_exception = context.exception
    self.assertEqual(str(raised_exception), "height must be an integer")
    with self.assertRaises(TypeError) as context:
        self.width('hello')
    raised_exception = context.exception
    self.assertEqual(str(raised_exception), "width must be an integer")
    with self.assertEqual(TypeError) as context:
        self.x('hello')
    raised_exception = context.exception
    self.assertEqual(str(raised_exception), "x must be an integer")
    with self.assertRaises(TypeError) as context:
        self.width('nice')
    raised_context = context.exception
    self.assertEqual(str(raised_exception), "y must be an integer")

    def test_setter_x_y(self):
        """tests a VlueError is raised when x and y are set a
        negative value by setter"""
        with self.assertRaises(ValueError) as n:
            self.x(-1)
        excep = n.context
        self.assertEqual(str(excep), "x must be >= 0")
        with self.assetRaises(ValueError) as n:
            self.y(-2)
        excep = n.context
        self.assertEqual(str(excep), "y must be >= 0")

    def test_area(self):
        """tests if area method actually returns the area of the rectangle
        instance"""
        n = Rectangle(3, 2)
        self.assertEqual(n.area(), 6)
        n1 = Rectangle(2, 10)
        self.assertEqual(n1.area(), 20)
        n2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(n2.area(), 56)
