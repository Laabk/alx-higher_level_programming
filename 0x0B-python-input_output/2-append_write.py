#!/usr/bin/python3
"""
this a module of a function for appending text to file
"""


def append_write(filename="", text=""):
    """
    this function appends text/char to ends of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as fil:
        return (fil.write(text))
