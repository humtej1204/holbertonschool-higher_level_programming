#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class for unittests"""
    def test_max_integer(self):
        """check possible cases edge cases"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([-12]), -12)
        self.assertEqual(max_integer([-1, -1, -1]), -1)
        self.assertEqual(max_integer([15, 1, 25]), 25)
        self.assertEqual(max_integer([15, 10, 5, -50, -100, -150]), 15)
        self.assertEqual(max_integer([15, 150, 1500]), 1500)

    def test_type_error(self):
        """type_errors"""
        self.assertRaises(TypeError, max_integer, ["h", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])
