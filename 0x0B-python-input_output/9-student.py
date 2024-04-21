#!/usr/bin/python3
"""defines a class student"""


class Student:
    """ class Student that defines a studen"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """etrieves a dictionary representation of a Student instance"""
        return student.__dict__
