#!/usr/bin/python3
"""
this functrions checks to an obj
is a instance of a_class
"""


def is_same_class(obj, a_class):
    """it return true if the ob is an instance of the
    class and flase if not
    """
    return (type(obj) == a_class)
