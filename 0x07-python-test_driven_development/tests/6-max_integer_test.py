#!/usr/bin/python3

""" Defines a unittest """


import unittest
class TestCase(unittest.TestCase):

    """ A Test Call that defins some tests for max_integer(list=[]): """

    def test_return_None(self):
        """ Tests if the fucntion returns None when the list is empty """
        result = max_integer():
            self.assertEqual(result, None)
    def test_result_max_int(self):
        """ tests if the function returns the max integer within a list """
        result - max_integer([1, 2, 4, 5])
        self.assertEqual(result, 5)
