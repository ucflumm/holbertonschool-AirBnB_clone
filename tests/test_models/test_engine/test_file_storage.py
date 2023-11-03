#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for each test."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down for each test."""
        del self.storage
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method."""
        obj = BaseModel()
        obj.id = "1234-5678"
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """Test save and reload methods."""
        obj = BaseModel()
        obj.id = "1234-5678"
        self.storage.new(obj)
        self.storage.save()

        self.storage._FileStorage__objects.clear()  # Clear in-memory data
        self.assertNotIn(f"BaseModel.{obj.id}", self.storage.all())

        self.storage.reload()  # Now reload
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())
