#!/usr/bin/python3
"""
A module that writes to a file using the JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that uses JSON method to Writes an object to a text-file"""
    with open(filename, "w") as fil:
        json.dump(my_obj, fil)
