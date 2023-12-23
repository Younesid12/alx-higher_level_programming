#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lin_1 in matrix:
        for colu in lin:
            print("{:d}".format(colu), end=" " if colu != lin_1[-1] else "")
        print()
