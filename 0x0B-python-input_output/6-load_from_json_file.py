#!/usr/bin/python3
"""
A module for creating using the JSON file representation
"""
import json


def load_from_json_file(filename):
    """
    this function Creates an object of python using a particular JSON file
    """
    with open(filename) as fil:
        return json.load(fil)
