#!/usr/bin/python3
"""checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """
    this function returns True if obj is an instance of a_class
    and False if otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
