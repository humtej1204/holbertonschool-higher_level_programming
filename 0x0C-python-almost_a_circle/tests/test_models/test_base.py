#!/usr/bin/python3
"""
Unittest to test all the methods of the class
Base to know if the methods are working correctly
"""
import unittest
import pycodestyle
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    A class to test Base Class
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pycodestyle.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_as_positive(self):
        """
        Test for positive Base Class id
        """
        base_instance = Base(110)
        self.assertEqual(base_instance.id, 110)
        base_instance = Base(30)
        self.assertEqual(base_instance.id, 30)

    def test_id_as_negative(self):
        """
        Test for negative Base Class id
        """
        base_instance = Base(-20)
        self.assertEqual(base_instance.id, -20)
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)

    def test_id_as_none(self):
        """
        Test for None Base Class id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base("Ping Pong")
        self.assertEqual(base_instance.id, "Ping Pong")
        base_instance = Base("Hola soy Goku")
        self.assertEqual(base_instance.id, "Hola soy Goku")

    def test_to_json_string(self):
        """
        Test to_json_string method
        """
        rect_instance = Rectangle(10, 17, 2, 8, 70)
        rect_data = re1.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """
        Test for a empty data on to_json_string method
        """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        """
        Test Base Class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """
        Test a normal to_json_string functionality
        """
        rect_data = {'id': 31, 'x': 14, 'y': 10, 'width': 5, 'height': 5}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 31, "x": 14, "y": 10, "width": 5, "height": 5]}'
        )

    def test_wrong_to_json_string(self):
        """
        Test a wrong functionality of to_json_string method
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_wrong_save_to_file(self):
        """
        Test save_to_file method
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

    def test_create(self):
        """
        Test create method
        """
        with self.assertRaises(TypeError) as msg:
            warn = Rectangle.create('Monty Python')

        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(msg.exception)
        )
