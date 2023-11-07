#!/usr/bin/python3
"""
this is module function which showes a text file insertion
"""


def append_after(filename="", search_string="", new_string=""):
    """
    this function inserts a text after a line containing a string in a file
    """
    th_text = ""
    with open(filename) as s:
        for line in s:
            th_text += line
            if search_string in line:
                th_text += new_string
    with open(filename, "w") as i:
        i.write(th_text)
