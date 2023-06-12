#!/usr/bin/python3

"""
A Class MyList that inherits the
attributes references of class list
    Args:
        list: class list
"""


class MyList(list):
    """
    The Class that inherits from the list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ The function that prints the sorted list """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
