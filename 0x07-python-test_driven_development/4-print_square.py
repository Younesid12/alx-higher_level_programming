#!/usr/bin/python3

""" Defines a function ."""

def print_square(size):
    """ prints a square with the character #.

    Args:
        size (int): the size length of the square.

    Returns:
        Nothing

    Raises:
        TypeError: soze must be an integer
        ValueError: size must be >= 0

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####
        >>> print_square(10)
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        >>> print_square(1)
        #
        >>> print_square(-1)
        Traceback (most recent call last):
        ...
        ValueError: size must be >= 0
        >>> print_square(-1.22)
        Traceback (most recent call last):
        ...
        TypeError: size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and not isinstance(size, float):
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(size):
            for _ in range(size):
                print("{}".format("#"), end='')
            print()
