#!/usr/bin/python3

"""File-appending Mode"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end
    of a text file (UTF8) and returns the number
    of characters added:
    Args:
        filename (str): Name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
