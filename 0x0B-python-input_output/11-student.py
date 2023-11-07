#!/usr/bin/python3
"""this defines a class Student."""


class Student:
    """that is a function for a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing the class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """takes dictionary representation of student and if the
        attrs is a list of strings, represents only those attributes
        included in the list.
        """
        if (type(attrs) == list and
                all(type(ele) == str for lis in attrs)):
            return {d: getattr(self, d) for d in attrs if hasattr(self, d)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        this changes/replace all attributes of the Student.
        """
        for d, a in json.items():
            setattr(self, d, a)
