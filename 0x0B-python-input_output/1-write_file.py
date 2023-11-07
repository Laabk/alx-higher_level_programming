#!/usr/bin/python3
"""
this module of a function which writes to a  file
"""


def write_file(filename="", text=""):
    """
    this function Writes a characters or string to the UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as fil:
        return fil.write(text)
