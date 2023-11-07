#!/usr/bin/python3
"""
A module showing a a representation of JSON object
"""


import json


def from_json_string(my_str):
    """
    this function returns an object representation of a JSON stringin python
    """
    return json.loads(my_str)
