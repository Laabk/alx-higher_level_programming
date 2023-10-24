#!/usr/bin/python3
"""defines a class square"""

class Square:
    """the class square"""

    def __init__(self, size=0):
        """initialising the class to store
        Args:
            size: size of the square
        Raises:
            TypeError and ValueError
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
