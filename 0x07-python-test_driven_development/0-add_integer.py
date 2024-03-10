#!/usr/bin/python3

""" defines a function of addition"""


def add_integer(a, b=98):

	""" this functions adds two integers
	a and b must be integers or floats otherwise a TypeError would raise
	examples:
	
	>>> add_integer(1, 2)
	3
	>>> add_integer(100, -2)
	98
	>>> add_integer(4, 'School')
	Traceback (most recent call last):
	...
	TypeError: b must be an integer
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
