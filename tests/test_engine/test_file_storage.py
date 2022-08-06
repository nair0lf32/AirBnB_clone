#!/usr/bin/python3
"""
test module for models/engine/file_storage.py.
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage class."""

    def setUp(self):
        """unittest setup method"""
        self.test_fs = FileStorage()
        self.test_bm = BaseModel()
        self.test_objs = FileStorage._FileStorage__objects
        self.test_file_path = "file.json"

    def test_instance(self):
        """Checks instance creation"""
        self.assertIsInstance(self.test_fs, FileStorage)

    def test_all(self):
        """Checks if all returns a dictionary"""
        self.assertEqual(dict, type(self.test_fs.all()))

    def test_new(self):
        """Checks if new adds an object to the FileStorage"""
        self.test_fs.new(self.test_bm)
        self.assertIn("BaseModel." + self.test_bm.id,
                      self.test_fs.all().keys())
        self.assertIn(self.test_bm, self.test_fs.all().values())

    def test_save(self):
        """Checks if save saves the FileStorage to a file"""
        self.test_fs.new(self.test_bm)
        self.test_fs.save()
        with open(self.test_file_path, "r") as f:
            self.assertIn("BaseModel." + self.test_bm.id, f.read())

    def test_reload(self):
        """Checks if reload loads the FileStorage from a file"""
        self.test_fs.new(self.test_bm)
        self.test_fs.save()
        self.test_fs.reload()
        self.assertIn("BaseModel." + self.test_bm.id, self.test_objs)


if __name__ == "__main__":
    unittest.main()
