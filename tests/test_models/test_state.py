#!/usr/bin/python3
"""Test for State Class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_state(self):
        """Check initialise state"""
        a = State()
        self.assertIsInstance(a, State)
        self.assertEqual(a.name, "")
