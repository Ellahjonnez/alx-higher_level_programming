#!/usr/bin/python3

""" a class MyList that inherits from list"""


class MyList(list):
    """ The Class that inherits from list"""

    def print_sorted(self):
        """ The function that prints the list,
        but sorted in ascending
        """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
