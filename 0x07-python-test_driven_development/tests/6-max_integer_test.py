#!/usr/bin/python3

"""Unittest for max_integer([..])

"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The following are different test cases
    for the max_integer function

    """
    def test_max(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([0, -1, -6, -2]), 0)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([-2, 4, -4, -9]), 4)
        self.assertAlmostEqual(max_integer([4, 5, 3]), 5)

    def test_input_type(self):
        self.assertRaises(TypeError, max_integer, True)

