#!/usr/bin/python3

"""a function that prints a square with the character #."""


def print_square(size):

    """To print a square with the character #.
    The Arguments:
        size: the size length of the square
 	size: must be of type (int)
    Raises exceptions:
        TypeError: size must be an integer
	> If size is not an integer.
        ValueError: size must be >= 0
	> If size is < 0
	TypeError: size must be an integer
	> If size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
