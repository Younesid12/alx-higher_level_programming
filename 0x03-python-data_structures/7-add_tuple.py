#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    modified_a = tuple_a + (0, 0)
    modified_b = tuple_b + (0, 0)
    new_tuple = modified_b[0] + modified_a[0], modified_a[1] + modified_b[1]
    return new_tuple
