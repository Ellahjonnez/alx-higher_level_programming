#!/usr/bin/python3

"""A function that divides all elements of a matrix."""


def matrix_divided(matrix, div):

    """
    To divide all elements of a matrix.
    Args:
        The matrix must be (A list of lists of ints or floats).
       Else......

    Raises TypeError Exception:

        TypeError: "Matrix must be a matrix (list of lists) of integers/floats"
        > If the matrix contains non-integer or no-float.
        TypeError: "Each row of the matrix must have the same size"
        > If the matrix contains rows of different sizes.
        TypeError: "div must be a number"
        > If div is not an int or a float.
        ZeroDivisionError: "division by zero"
        > If div is 0.
    Returns: A new matrix.

    """

    # Check if matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and
               all(isinstance(num, (int, float))
                   for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of"
                        "integers/floats")

    # Check if each row of the matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round the result to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
