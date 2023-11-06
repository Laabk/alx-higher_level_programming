#!/usr/bin/python3
"""this functions checks to ensure if obj
is an instance of a_class
"""


def is_kind_of_class(obj, a_class):
    """it returns true if obj is an instance of a class
    but otherwise it returns false
    """
    return (isinstance(obj, a_class))
