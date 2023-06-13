#!/usr/bin/python3

"""Load, add, save to a Python list"""

import sys
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    with open(filename, "r") as file:
        return json.load(file)


args = sys.argv[1:]
# Get command-line arguments excluding the script name

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

my_list.extend(args)

save_to_json_file(my_list, "add_item.json")
