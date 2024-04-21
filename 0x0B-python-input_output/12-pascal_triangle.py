#!/usr/bin/python3
"""defines a funcion"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        s = triangle[-1]
        tmp = [1]
        for i in range(len(s) - 1):
            tmp.append(s[i] + s[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
