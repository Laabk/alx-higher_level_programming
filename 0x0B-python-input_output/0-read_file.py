#!/usr/bin/python3
"""
this module of a function which reads text-file
"""


def read_file(filename=""):
    """this then reads the info UTF8 text-file"""
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
