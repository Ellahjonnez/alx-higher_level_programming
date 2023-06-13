#!/usr/bin/python3
"""JSON Save Object to a file Mode"""

import json


def save_to_json_file(my_obj, filename):
    """A function that write an object to
     a text file using JSON representation.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
