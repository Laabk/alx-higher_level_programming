#!/usr/bin/python3
"""a  module which defines a function which adds attributes to objects"""


def add_attribute(obj, att, value):
    """
    this funct add a new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
