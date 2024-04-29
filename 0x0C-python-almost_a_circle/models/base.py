#!/usr/bin/python3
"""defines a base class"""

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes instance attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return '[]'
        data = json.dumps(list_dictionaries)
        return data

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if not list_objs:
            data = []
        else:
            data = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding='UTF-8') as n:
            n.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if 'width' in dictionary:
            n = cls(1, 2)
        else:
            n = cls(1)
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls}" + ".json"
        try:
            n = open(filename, 'r', encoding='UTF-8')
        except FileNotFoundError:
            return []
        else:
            a = from_json_string(n.read())
            n.close()
            return [Base.create(**d) for d in a]
