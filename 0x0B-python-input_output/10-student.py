#!/usr/bin/python3
"""
this is a module of a funfunction for a class Student
"""


class Student:
    """this represent the class student."""

    def __init__(self, first_name, last_name, age):
        """Initializing the class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """takes a dictionary representation of Student and if attrs is
        a list of strings, it represents only those attributes in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ite in attrs)):
            return {d: getattr(self, d) for d in attrs if hasattr(self, d)}
        return self.__dict__
