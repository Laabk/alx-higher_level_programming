#!/usr/bin/python3
"""
a module which defines a class MyInt inherited from the class int
"""


class MyInt(int):
    """
    an inherited class of the class  int
    """

    def __eq__(self, other):
        """
        this method returns != as check
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ this method returns == as check """
        return int.__eq__(self, other)
