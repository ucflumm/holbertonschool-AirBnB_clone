#!/usr/bin/python3
"""Test for City Class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_init(self):
        """Check initialise city"""
        a = City()
        self.assertIsInstance(a, City)
        self.assertEqual(a.name, "")
        self.assertEqual(a.state_id, "")
