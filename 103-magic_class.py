#!/usr/bin/python3
"""peinting a docstring"""
import math


class MagicClass:
    """initialising the cllaas magic"""

    def __init__(self, radius=0):
        """ defining rhe docstring """
        self.__radius = 0
        if type(radius) is not float and type(radius) is not int:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
