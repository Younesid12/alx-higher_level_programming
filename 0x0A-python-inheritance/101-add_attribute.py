#!/usr/bin/python3
""" defines a function"""


def add_attribute(self, name, value):
    self.__init__(name, value):
        self.name = value
        if type(self.name) is not MyClass:
            raise TypeError("can't add new attribute")
