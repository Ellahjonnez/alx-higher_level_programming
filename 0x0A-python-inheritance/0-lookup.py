#!/usr/bin/python3

"""
a function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """Function that get the list of
       attributes and methods of the object
    """
    attributes = [attr for attr in dir(obj)
                  if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj)
               if callable(getattr(obj, method))]

    # Combine and return the list
    return attributes + methods
