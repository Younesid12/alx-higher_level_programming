#!/usr/bin/python3
"""defines inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class ; otherwise False."""
    return type(obj) is not a_class issubclass(obj, a_class)
