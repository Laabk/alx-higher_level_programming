#!/usr/bin/python3
"""
this is module trhat inherits the class from list class
"""


class MyList(list):
    """the inherited list class"""
    def print_sorted(self):
        """this methods prints sorted list"""
        print(sorted(self))
