#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ Creating a new matrix by applying the square 
    function to each element using lambda and map"""

    result = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))

    return (result)
