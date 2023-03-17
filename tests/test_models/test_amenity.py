#!/usr/bin/python3
"""Test for Amenity Class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test instances and methods from amenity class."""

    a = Amenity()

    def test_class_exists(self):
        """Test if class exists."""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)
