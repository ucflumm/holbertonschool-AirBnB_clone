#!/usr/bin/python3
"""Test for Review Class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_review(self):
        """Check initialise review"""
        a = Review()
        self.assertIsInstance(a, Review)
        self.assertEqual(a.place_id, "")
        self.assertEqual(a.user_id, "")
        self.assertEqual(a.text, "")
