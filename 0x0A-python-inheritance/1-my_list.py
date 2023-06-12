#!/usr/bin/python3

"""
A Class MyList that inherits the
attributes references of class list
"""


class MyList(list):
    """
    The Class that inherits from the list
    """

    def print_sorted(self):
        """ The function that prints the sorted list """
        print(sorted(self))
