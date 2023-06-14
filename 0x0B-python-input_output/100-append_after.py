#!/usr/bin/python3

"""Module for Search and update method."""


def append_after(filename="", search_string="", new_string=""):
    """
     A function that inserts a line of text to a file, after
     each line containing a specific string (see example):

    Arguments:
        filename {str} >> name of file
        search_string {str} >> string to search for
        new_string {str} >> string to insert
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
