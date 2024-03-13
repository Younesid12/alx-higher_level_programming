#!/usr/bin/python3

"""Define a faunction of addition of integers"""


def add_integer(a, b=98):   
   """
    This function adds two integers.

    Args:
	    a (int or float): The first number.
	    b (int or float): The second number (default is 98).
    Returns:
            int: The sum of a and b.

    Raises:
	    TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(1, 2)
	3
	>>> add_integer(100, -2)
	98
	>>> add_integer(2)
	100
	>>> add_integer(100.3, -2)
	98
	>>> add_integer(4, "School")
	Traceback (most recent call last):
	...
	TypeError: b must be an integer
	>>> add_integer(None)
	Traceback (most recent call last):
	...
	TypeError: a must be an integer
        """
    if not isinstance(a, (int, float)):
	    raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
	    raise TypeError("b must be an integer")
    if isinstance(a, float):
	    a = int(a)
    elif isinstance(b, float):
	    b = int(b)
    return a + b
