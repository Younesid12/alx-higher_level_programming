#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lin_1 in matrix:
        for colu in lin:
            print("{:d}".format(col), end=" " if col != lin[-1] else "")
        print()
