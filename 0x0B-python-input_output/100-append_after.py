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

    with open(filename, 'r+') as file:
        lines = file.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        file.seek(0)
        file.writelines(new_lines)
