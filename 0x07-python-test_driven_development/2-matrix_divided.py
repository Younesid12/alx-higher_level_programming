#!/usr/bin/python3

"""Defines a function that devides all elements of a matrix. """


def matrix_divided(matrix, div):
   
    """
    Divides all elements of a matrix.

    Args:
        matrix: list of lists containing only float and integers
        div: must be a number of (integer float not 0), divisive number

    Returns:
        a new matrix composining of those numbers divided by div

    Examples:
        >>> matrix = [
        ... [1, 2, 3],
        ... [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> print(matrix)
        [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided([[1, 2, 3], [4, 5, 6, 7]], 3)
        Traceback: (most recent call last):
        ...
        TypeError: Each row of the matrix must have the same size
        >>> matrix_divided([[1, 2, 3], ['h']], 2)
        Traceback: (most recent call last):
        ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 0)
        Traceback: (most recent call last)
        ...
        ZeroDivisionError: division by zero
        >>> matrix_divided(matrix, 'h')
        Traceback: (most recent call last):
        ...
        TypeError: div must be a number
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(map(lambda row: all(isinstance(x, (int, float)) for x in row), matrix)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix[0])
    if not all(len(matrix[n]) == length for n in range(1, len(matrix))):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
            raise TypeError("div must be a number")
    if div == 0:
            raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
