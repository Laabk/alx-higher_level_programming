#!/usr/bin/python3
class Square:
    """defines a clas square"""

    def __init__(self, size=0):
        """Initializing the square class
        Args:
            size: the size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """this takes the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        "returns the area of the square"
        return (self.__size ** 2)

    def my_print(self):

        if self.__size == 0:
            print()

        for d in range(self.__size):
            print("#" * self.__size)
