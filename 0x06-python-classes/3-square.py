#!/usr/bin/python3
"""define a class of square """


class Square():
    """initializing the the size of the square"""
    def __init__(self, size=0):
        """values of private attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of square"""
        return self.__size ** 2
