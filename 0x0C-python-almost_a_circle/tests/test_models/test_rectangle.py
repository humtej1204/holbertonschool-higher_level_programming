#!/usr/bin/python3
"""
Unittest to test all the methods of the class
Rectangle to know if the methods are working correctly
"""


import unittest
import io
import json
import pycodestyle
import os
from models import square
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout
Square = square.Square


class TestCodeFormat(unittest.TestCase):
    def test_pycodestyle(self):
        """Test that we conform to PEP-8"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class testcases(unittest.TestCase):
    """Testing square class"""
    @classmethod
    def setUpClass(cls):
        Base.__Base_objects = 0
        cls.c1 = Square(1)
        cls.c2 = Square(2, 3)
        cls.c3 = Square(3, 4, 5)
        cls.c4 = Square(5, 6, 7)
        cls.c5 = Square(7, 8, 9, 10)
        cls.c1.id = 1
        cls.c2.id = 2
        cls.c3.id = 3
        cls.c4.id = 4
        cls.c5.id = 10

    def test_square_instance(self):
        """Test if square is instance of Rectangle and Base"""
        s6 = Square(5, 2, 1, 20)
        self.assertEqual(type(s6), Square)
        self.assertFalse(type(s6) == Rectangle)
        self.assertFalse(type(s6) == Base)
        self.assertTrue(isinstance(s6, Base))
        self.assertTrue(isinstance(s6, Rectangle))
        self.assertTrue(isinstance(s6, Square))

    def test_size(self):
        self.assertEqual(self.c1.size, 1)
        self.assertEqual(self.c2.size, 2)
        self.assertEqual(self.c3.size, 3)
        self.assertEqual(self.c4.size, 5)
        self.assertEqual(self.c5.size, 7)

    def test_height(self):
        self.assertEqual(self.c1.height, 1)
        self.assertEqual(self.c2.height, 2)
        self.assertEqual(self.c3.height, 3) 
        self.assertEqual(self.c4.height, 5)
        self.assertEqual(self.c5.height, 7)

    def test_x(self):
        self.assertEqual(self.c1.x, 0)
        self.assertEqual(self.c2.x, 3)
        self.assertEqual(self.c3.x, 4)
        self.assertEqual(self.c4.x, 6)
        self.assertEqual(self.c5.x, 8)

    def test_y(self):
        self.assertEqual(self.c1.y, 0)
        self.assertEqual(self.c2.y, 0)
        self.assertEqual(self.c3.y, 5)
        self.assertEqual(self.c4.y, 7)
        self.assertEqual(self.c5.y, 9)

    def test_arg(self):
        with self.assertRaises(TypeError):
            s = Square()

    def testing_size_typeError(self):
        """Testing typerror error for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("luffy")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(False)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([1, 3])

    def testing_size_valueerror(self):
        """Testing value error for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def testing_x_valuerror(self):
        """testing value for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def testing_y_valuerror(self):
        """testing value for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_area(self):
        """Testing area, assigments comes from lines 19"""
        self.assertEqual(self.c1.area(), 1)
        self.assertEqual(self.c2.area(), 4)
        self.assertEqual(self.c3.area(), 9)
        self.assertEqual(self.c4.area(), 25)
        self.assertEqual(self.c5.area(), 49)

    def test_area_args(self):
        """we just can call area, not pass args"""
        with self.assertRaises(TypeError):
            self.c1.area(1)

    def test_display_arg(self):
        """we just can call display, no pars args"""
        with self.assertRaises(TypeError):
            self.c1.display(1)



    def test_update_kwargs_setter(self):
        """testing setters with kwargs"""
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size=[3, 4])
        with self.assertRaises(TypeError):
            s.update(x="luffy")
        with self.assertRaises(TypeError):
            s.update(y="monkey")

        with self.assertRaises(ValueError):
            s.update(size=-2)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-2)
        with self.assertRaises(ValueError):
            s.update(y=-2)

    def test_to_dict(self):
        """Testing dictionary"""
        test1 = self.c1.to_dictionary()
        # self.assertEqual({"id": 1, "size": 1, "x": 0, "y": 0}, test1)
        test2 = self.c2.to_dictionary()
        # self.assertEqual({"id": 2, "size": 2, "x": 3, "y": 0}, test1)
        test3 = self.c3.to_dictionary()
        # self.assertEqual({"id": 3, "size": 3, "x": 4, "y": 5}, test1)
        test4 = self.c4.to_dictionary()
        # self.assertEqual({"id": 4, "size": 5, "x": 5, "y": 7}, test4)
        self.assertTrue(type(test1) is dict)
        self.assertTrue(type(test2) is dict)
        self.assertTrue(type(test3) is dict)
        self.assertTrue(type(test4) is dict)
        test5 = Square(1, 1, 1, 1)
        test5.update(**test4)
        self.assertEqual(str(test5), str(self.c4))
        self.assertNotEqual(test5, self.c4)

    def test_save_to_file(self):
        """Testing save_to_file"""
        test1 = Square(1, 1, 1, 1)
        test2 = Square(2, 2, 2, 2)
        l = [test1, test2]
        Square.save_to_file(l)
        with open("Square.json", "r") as file:
            ls = [test1.to_dictionary(), test2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_empty_str(self):
        """pasing empy string"""
        l = []
        Square.save_to_file(l)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_none_str(self):
        """parsing none"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_load_f_file(self):
        """testing normal cases load file"""
        test1 = Square(2, 3, 4, 5)
        test2 = Square(7, 8, 9, 10)
        li = [test1, test2]
        Square.save_to_file(li)
        lo = Square.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        test1c = lo[0]
        test2c = lo[1]
        self.assertTrue(type(test1c) is Square)
        self.assertTrue(type(test2c) is Square)
        self.assertEqual(str(test1), str(test1c))
        self.assertEqual(str(test2), str(test2c))
        self.assertIsNot(test1, test1c)
        self.assertIsNot(test2, test2c)
        self.assertNotEqual(test1, test1c)
        self.assertNotEqual(test2, test2c)
