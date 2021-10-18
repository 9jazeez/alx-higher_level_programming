#!/usr/bin/python3

"""Testing the base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """using assert to test """
    def testRectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
        base2 = Base()
        self.assertEqual(base2.id, 4)
        r2 = Rectangle(12, 2, id=12)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(4, 6)
        self.assertEqual(r3.id, 5)
