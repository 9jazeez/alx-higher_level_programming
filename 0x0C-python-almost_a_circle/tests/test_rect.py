#!/usr/bin/python3

"""Testing the rectangle class"""


import unittest
import os
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """using assert to test """

    def setUp(self):
        Base.__Base__nb_objects = 0

    def testCase1(self):
        """Test Case 1"""
        r = Rectangle(10, 2)
        self.assertTrue(isinstance(r, Base))

    def testCase2(self):
        """Test Case 2"""
        r1 = Rectangle(10, 5, id=2)
        self.assertEqual(r1.id, 2)
        r2 = Rectangle(12, 2, id=12)
        self.assertEqual(r2.id, 12)

    def testCase3(self):
        """checking error messages"""
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle("10", 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def testCase4(self):
        """Checking Error prompts"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(float("nan"), 1)
        self.assertEqual("width must be an integer", str(err.exception))

    def testCase5(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(float("inf"), 20)
        self.assertEqual("width must be an integer", str(err.exception))

    def testCase6(self):
        """Test for None input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(None)
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", str(err.exception))

    def testCase7(self):
        """Test for int input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(20)
        self.assertEqual("__init__() missing 1 required positional argument: 'height'", str(err.exception))

    def testCase8(self):
        """Test for empty input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle()
        self.assertEqual("__init__() missing 2 required positional arguments: 'width' and 'height'", str(err.exception))

    def testCase9(self):
        """Test 9"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(20, "20")
        self.assertEqual("height must be an integer", str(err.exception))

    def testCase10(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(30, 20, "x")
        self.assertEqual("x must be an integer", str(err.exception))

    def testCase11(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, 20, 12, "y")
        self.assertEqual("y must be an integer", str(err.exception))

    def testCase12(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(12.4, 20)
        self.assertEqual("width must be an integer", str(err.exception))

    def testCase13(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(20, 20.3)
        self.assertEqual("height must be an integer", str(err.exception))

    def testCase14(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, 20, 10.4)
        self.assertEqual("x must be an integer", str(err.exception))

    def testCase15(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, 20, 0, 0.2)
        self.assertEqual("y must be an integer", str(err.exception))

    def testCase16(self):
        """Test for int input"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, -4)
        self.assertEqual("height must be > 0", str(err.exception))

    def testCase17(self):
        """Test for int input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle([], 20, 0, 0.2)
        self.assertEqual("width must be an integer", str(err.exception))

    def testCase18(self):
        """Test for int input"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(-10, 4)
        self.assertEqual("width must be > 0", str(err.exception))

    def testCase19(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, [1, 2], 0, 0.2)
        self.assertEqual("height must be an integer", str(err.exception))

    def testCase20(self):
        """Test for int input"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, 4, -5)
        self.assertEqual("x must be >= 0", str(err.exception))

    def testCase21(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, 20, {'x': 0, 'y': 0})
        self.assertEqual("x must be an integer", str(err.exception))

    def testCase22(self):
        """Test for int input"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, 4, 0, -2)
        self.assertEqual("y must be >= 0", str(err.exception))

    def testCase23(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle(10, 20, 0, [])
        self.assertEqual("y must be an integer", str(err.exception))

    def testCase24(self):
        """Test for int input"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(10, 0)
        self.assertEqual("height must be > 0", str(err.exception))

    def testCase25(self):
        """Test for inf input"""
        with self.assertRaises(TypeError) as err:
            r = Rectangle([2, 5], 20, 0, 0.2)
        self.assertEqual("width must be an integer", str(err.exception))

    def testCase26(self):
        """Test for int input"""
        with self.assertRaises(ValueError) as err:
            r = Rectangle(0, 40)
        self.assertEqual("width must be > 0", str(err.exception))

    def testCase27(self):
        """Test 21 for Rectangle"""
        r = Rectangle(12, 14, 1, 9)
        r_dict = {'x': 1, 'y': 9, 'id': 21, 'height': 14, 'width': 12}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)
        r = Rectangle(12, 12, 15)
        r_dict = {'width': 12, 'height': 12, 'x': 15, 'id': 22, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)
        r = Rectangle(62, 414)
        r_dict = {'width': 62, 'height': 414, 'x': 0, 'id': 23, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = {'width': 1, 'height': 2, 'x': 3, 'id': 5, 'y': 4}
        self.assertEqual(r.to_dictionary(), r_dict)
        self.assertEqual(r.to_dictionary() is r_dict, False)


    def testCase28(self):
        """Test 21 for Rectangle"""
        r = Rectangle(1, 2, 3, 4, 12)
        r.update()
        self.assertEqual(r.__str__(), "[Rectangle] (12) 3/4 - 1/2")

    def testCase29(self):
        """Test 19 for Rectangle"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=12)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/12")
        r.update(width=12, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 12/12")
        r.update(y=1, width=2, x=3, id=112)
        self.assertEqual(r.__str__(), "[Rectangle] (112) 3/1 - 2/12")

    def testCase30(self):
        """Test 30 for Rec"""
        r = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        s = f.getvalue()
        o = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(s, o)
        r = Rectangle(3, 2, 0, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()s = f.getvalue()
        o = "###\n###\n"
        self.assertEqual(s, o)

    def testCase31(self):
        """Test 18 for Rectangle"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 10/10 - 10/10")
        r.update(67, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (67) 10/10 - 2/10")
        r.update(68, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (68) 10/10 - 3/4")
        r.update(98, 12, 9, 8)
        self.assertEqual(r.__str__(), "[Rectangle] (98) 8/10 - 12/9")
        r.update(14, 22, 13, 11, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (14) 11/12 - 22/13")
        r = Rectangle(1, 1)
        r.update(76, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (76) 4/5 - 2/3")
