#!/usr/bin/python3
"""Test for Amenity Class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_init(self):
        """Check initialise amenity"""
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_name(self):
        """Check Amenity name"""
        a = Amenity()
        a.name = "Babychair"
        self.assertEqual(a.name, "Babychair")
