#!/usr/bin/python3

"""A Python class-to-JSON Mode"""


def class_to_json(obj):

    """
     A function that returns the dictionary description with simple
     data structure (list, dictionary, string, integer and boolean)
     for JSON serialization of an object:
    """
    attributes = obj.__dict__
    json_dict = {}
    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value
    return json_dict
