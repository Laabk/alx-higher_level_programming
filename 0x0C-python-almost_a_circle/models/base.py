#!/usr/bin/python3

"""this models represents a base class of those created."""
import json
import csv
import turtle


class Base:
    """the class base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the instance of the of the new base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this return serialization of JSON dictionary_list"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this saves  serials of JSON list of objects in a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return JSON list of objects created in a string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class from a dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return class list instantiated from a file of JSON strings"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves the CSV serial of list of objects to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a class list instantiated from the CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """this draw Rectangles and Squares using the turtle module"""
        tut = turtle.Turtle()
        tut.screen.bgcolor("#b7312c")
        tut.pensize(3)
        tut.shape("turtle")

        tut.color("#ffffff")
        for reta in list_rectangles:
            tut.showturtle()
            tut.up()
            tut.goto(reta.x, reta.y)
            tut.down()
            for d in range(2):
                tut.forward(reta.width)
                tut.left(90)
                tut.forward(reta.height)
                tut.left(90)
            tut.hideturtle()

        tut.color("#b5e3d8")
        for sqa in list_squares:
            tut.showturtle()
            tut.up()
            tut.goto(sqa.x, sqa.y)
            tut.down()
            for d in range(2):
                tut.forward(sqa.width)
                tut.left(90)
                tut.forward(sqa.height)
                tut.left(90)
            tut.hideturtle()

        turtle.exitonclick()
