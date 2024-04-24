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
