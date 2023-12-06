#!/usr/bin/python3
def square_matrix_simple(input_matrix=[]):
    result_square = [[n ** 2 for n in row] for row in input_matrix]
    return result_square
