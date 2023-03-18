#!/usr/bin/python3
"""Test for City Class."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test instances and methods from City class."""

    a = City()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance(self):
        """Test inheritance."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_name_attribute(self):
        """Test the attribute name."""
        city = City()
        self.assertTrue(hasattr(self.city, 'name'))

    def test_id_attribute(self):
        """Test if City has a state id attribute."""
        self.assertTrue(hasattr(self.city, 'state id'))

    def test_to_dict_method(self):
        """Test if to dict method produces dictionary."""
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))

    def test_str_method(self):
        """Test if __str__ mehtod produces string representation"""
        city_str = str(self.city)
        self.assertTrue(isinstance(city_str, str))
