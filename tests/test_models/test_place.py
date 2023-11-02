#!/usr/bin/python3
"""Test for Place Class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_init(self):
        """Check initialise place"""
        a = Place()
        self.assertIsInstance(a, Place)
        self.assertEqual(a.city_id, "")
        self.assertEqual(a.name, "")
        self.assertEqual(a.description, "")
        self.assertEqual(a.number_rooms, 0)
        self.assertEqual(a.number_bathrooms, 0)
        self.assertEqual(a.max_guest, 0)
        self.assertEqual(a.price_by_night, 0)
        self.assertEqual(a. latitude, 0.0)
        self.assertEqual(a.longitude, 0.0)
        self.assertEqual(a.amenity_ids, [])
