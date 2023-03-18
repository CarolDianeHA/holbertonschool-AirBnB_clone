#!/usr/bin/python3
"""Test for Amenity Class."""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test instances and methods from amenity class."""

    a = Amenity()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance(self):
        """Test inheritance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name_attribute(self):
        """Test the attribute name."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, '')
