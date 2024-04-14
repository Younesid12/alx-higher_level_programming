#!/usr/bin/python3
""" defines a class named my_list"""


class MyList(list):
    """list-inherited class"""
    def print_sorted(self):
        """prints the list  in a sorted manner"""
        print(sorted(self))
