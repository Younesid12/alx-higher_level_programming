#!/usr/bin/python3
"""defines a class student"""


class Student:
    """ class Student that defines a studen"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        data = {}
        if type(attrs) is list and all(type(element) == str for element in attrs):
            for value in attrs:
                if value in self.__dict__:
                    data[value] = self.__dict__[value]
        if len(data) == 0:
            return self.__dict__
        return data
