#!/usr/bin/python3


"""
Module that contains class for Student

"""


class Student:
    """A class for Student with init and to_json
    methods

    """

    def __init__(self, first_name, last_name, age):
        """Initialize"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary pattern"""
        return (self.__dict__)
