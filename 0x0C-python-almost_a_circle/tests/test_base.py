#!/usr/bin/python3

"""Testing the base class"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """using assert to test """
    def testBase(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(12)
        self.assertEqual(base3.id, 12)
