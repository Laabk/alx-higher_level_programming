#!/usr/bin/python3
"""
this function defines base geometry class
"""


class BaseGeometry:
    """
    a funct that represents a base geometry class
    """

    def area(self):
        """method for  implementing the  area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        ensures a value is an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
