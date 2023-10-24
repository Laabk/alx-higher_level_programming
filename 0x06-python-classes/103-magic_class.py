#!/usr/bin/python3
"""printing a docstring"""
import math


class MagicClass:
    """initialing that  of magic"""

    def __init__(self, radius=0):
        """a docstring """
        self.__radius = 0
        if type(radius) is not float and type(radius) is not int:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
