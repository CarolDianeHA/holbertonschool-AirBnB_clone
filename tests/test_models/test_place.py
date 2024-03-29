#!/usr/bin/python3
"""Test for Place Class."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test instances and methods from Place class."""

    a = Place()

    def setUp(self):
        self.a = Place()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.a)), res)


if __name__ == '__main__':
    unittest.main()
