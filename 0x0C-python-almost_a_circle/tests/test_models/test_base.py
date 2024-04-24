#!/usr/bin/python3
"""unitest for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests if __init__ actually initializes id
    with the value passed and if no value passed __nb_objects
    should be incremented and id should be assigned the
    value of the class attribute __nb_objects"""
    def test_id_not_passed(self):
        """tests if the instance atrribute id is given the
        value of the class atribute __nb_objects after incrementing
        it after no value is passed"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)

    def test_id_passed(self):
        """checks if id attribute is assigned the value passed and
        no increment to the public __nb_objects is done"""
        a = Base(12)
        self.assertEqual(a.id, 12)
        b = Base(14)
        self.assertEqual(b.id, 14)

if __name__ == '__main__':
    unittest.main()
