#!/usr/bin/python3

"""Defines a function that prints the fullname"""


def say_my_name(first_name, last_name=""):

    """
    prints the fullname.

    Args:
        first_name (str): the first name, only strings are accepted
        last_name (str, optional): the last name, should be a string, Defualt is an empty str

    Returns:
        nothing

    Raises:
        TypeError: if the arguemnt passed is not a string

    Examples:
        >>> say_my_name('Younes', 'Idomar')
        My name is Younes Idomar
        >>> say_my_name('Younes') # doctest: +NORMALIZE_WHITESPACE
        My name is Younes
        >>> say_my_name(2, 'Idomar')
        Traceback (most recent call last):
        ...
        TypeError: first_name must be a string
        >>> say_my_name('Younes', 4)
        Traceback (most recent call last):
        ...
        TypeError: last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
