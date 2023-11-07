#!/usr/bin/python3
"""
this modulerepresence a class Student
"""


class Student:
    """
    this function defines the clsaa student.
    """

    def __init__(self, first_name, last_name, age):
        """
        initializing the class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns the dictionary of the studencts instance
        """
        return self.__dict__
