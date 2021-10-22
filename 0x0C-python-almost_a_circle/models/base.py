#!/usr/bin/python3

"""
Module with base class

"""

import json
import os
import csv
import turtle
from os import path


class Base:
    """ Base class with private attr """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base Initializer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON TO STRINGS"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        if type(list_dictionaries) != list:
            raise TypeError("List_Dictionaries must be a list")
        if any(type(i) != dict for i in list_dictionaries):
            raise TypeError("list_dictionaries must contain dictionaries")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writing list to a file"""
        if type(list_objs) != list and list_objs is not None:
            raise TypeError("list_objs must be a list")
        if list_objs is None or list_objs == []:
            out = []
        else:
            first = type(list_objs[0])
            if any(type(i) != first for i in list_objs):
                raise ValueError("all elements of list_objs must match")
            out = [i.to_dictionary() for i in list_objs]
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            f.write(cls.to_json_string(out))

    @staticmethod
    def from_json_string(string):
        """return a string from a json"""
        if string is None or string == "":
            return ([])
        if type(string) != str:
            raise TypeError("json_string must be a string")
        data = json.loads(string)
        for d in data:
            if type(d) != dict:
                raise ValueError("json_string must contain dictionaries")

        return (data)

    @classmethod
    def create(cls, **dictionary):
        """instances"""
        aux = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        aux.update(**dictionary)

        return (aux)

    @classmethod
    def load_from_file(cls):
        """list of instances"""
        filename = str(cls).split(".")[-1][:-2] + ".json"
        if not os.path.exists(filename):
            return []
        ret = []
        with open(filename, "r") as f:
            dictionary = cls.from_json_string(f.readline())
        for x in dictionary:
            ret.append(cls.create(**x))

        return (ret)

    @classmethod
    def save_to_file_csv(cls, data):
        """CSV sterilization"""
        if type(data) != list and data is not None:
            raise TypeError("list_objs must be a list")
        if not all(isinstance(i, cls) for i in data):
            raise TypeError("list_objs must be a list")
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if data is not None:
                data = [i.to_dictionary() for i in data]
                sfields = ['id', 'size', 'x', 'y']
                rfields = ['id', 'width', 'height', 'x', 'y']

                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rfields)
                else:
                    writer = csv.DictWriter(f, fieldnames=sfields)
                writer.writeheader()
                writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """CSV desterilizer"""
        filename = cls.__name__ + ".csv"
        sheader = ["id", "size", "x", "y"]
        rheader = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Rectangle":
            header = rheader
        else:
            header = sheader

        result = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter='.')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for x, y in enumerate(row):
                            if y:
                                setattr(new, header[x], int(y))
                        result.append(new)

        return (result)

    @staticmethod
    def draw(list_rectangle, list_square):
        """A function that draw shapes using turtle
        library.

        Args:
        list_rectangle (Rectangle): first list
        list_square (Square): second list

        """
        border = 0
        big_h = 0
        big_w = 0

        for i in list_rectangle:
            big_w = i.width if i.width >= big_w else big_w
            big_h = i.height if i.height >= big_h else big_h

        for i in list_square:
            big_w = i.width if i.width >= big_w else big_w
            big_h = i.height if i.height >= big_h else big_h

        screen_w = 600 if big_w <= 500 else big_w
        screen_h = 600 if big_h <= 500 else big_h

        windows = turtle.Screen()
        windows.setup(screen_w, screen_h, 100, 100)
        windows.title("Shape Drawwing")
        windows.bgcolor('black')

# drawig border line
        border = screen_w / 2
        b = turtle.Turtle()
        b.color('yellow')
        b.pensize(2)
        b.hideturtle()
        b.penup()
        b.setpos(-(border - 10), (border - 10))
        b.pendown()
        b.fd(screen_w - 20)
        b.rt(90)
        b.fd(screen_h - 20)
        b.rt(90)
        b.fd(screen_w - 20)
        b.rt(90)
        b.fd(screen_h - 20)
        b.rt(90)
        b.penup()

        t = turtle.Turtle()
        side_count = 0
        t.color('cyan')
        t.penup()
        t.pensize(3)
        c = b.position()
        t.setpos(c)
        get_pos = t.pos()[1]

        for i in list_rectangle:
            if side_count >= border * 2:
                t.penup()
                t.setpos(-(border - 10), get_pos - 10)
                side_count = 0
            t.begin_fill()
            t.fillcolor('red' if i.width == i.height else 'cyan')
            t.pendown()
            t.fd(i.width)
            t.rt(90)
            t.fd(i.height)
            t.rt(90)
            t.fd(i.width)
            get_pos = t.pos()[1] if i.height > get_pos else get_pos
            t.rt(90)
            t.fd(i.height)
            t.rt(90)
            t.end_fill()
            t.penup()
            t.fd(i.width + 5)
            side_count += (i.width + 5)
        get_pos = 0
        t.setpos(-(border - 10), 0)
        side_count = 0

        for i in list_square:
            if side_count >= border * 2:
                t.penup()
                t.setpos(-(border - 10), -(50 - get_pos))
                side_count = 0
            t.begin_fill()
            t.fillcolor('red' if i.width == i.height else 'cyan')
            t.pendown()
            t.fd(i.width)
            t.rt(90)
            t.fd(i.height)
            t.rt(90)
            t.fd(i.width)
            get_pos = t.pos()[1] if i.height < get_pos else get_pos
            t.rt(90)
            t.fd(i.height)
            t.rt(90)
            t.end_fill()
            t.penup()
            t.fd(i.width + 5)
            side_count += (i.width + 5)

        windows.exitonclick()
