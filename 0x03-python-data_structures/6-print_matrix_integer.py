#!/usr/bin/python3

# to function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print('')
