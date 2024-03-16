#!/usr/bin/python3

""" Defines a unittest """


import unittest
class TestMaxInteger(unittest.TestCase):

    """ A Test Call that defins some tests for max_integer(list=[]): """

    def test_return_None(self):
        """ Tests if the fucntion returns None when the list is empty """
        result = max_integer()
        self.assertEqual(result, None)
    def test_at_the_end(self):
        """ tests if the function returns the max integer within a list """
        result - max_integer([1, 2, 4, 5])
        self.assertEqual(result, 5)
    def test_max_at_the_beginning(self):
        """ tests the function if it returns the max int that is in the beginning """
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)
    def test_max_in_the_middle(self):
        """ tests if the function returns the max value this is in the middle of the list"""
        self.assertEqual(max_integer([3, 12, 2]),12)
    def test_negative_num(self):
        """ tests the function when it recieves only negative numbers"""
        self.asserEqual(max_integer([-1, -2, -4]), -1)
    def test_one_negative(self):
        """ tests if works when recieving a list of positive values with only one negative value """
        self.assertEqual(max_integer([1, 2, -3]), 2)
    def test_one_elem(self):
        """ tests the function when it recieves a list of only one element"""
        self.assertEqual([2], 2)
