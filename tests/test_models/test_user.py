#!/usr/bin/python3
"""Test for State User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user(self):
        """Check initialise user"""
        a = User()
        self.assertIsInstance(a, User)
        self.assertEqual(a.email, "")
        self.assertEqual(a.password, "")
        self.assertEqual(a.first_name, "")
        self.assertEqual(a.last_name, "")
