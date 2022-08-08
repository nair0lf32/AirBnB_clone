#!/usr/bin/python3
"""
test module for models/base_model.py.
"""

import unittest
import time
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """testing the BaseModel class."""

    def setUp(self):
        """unittest setup method"""
        self.test_bm = BaseModel()
        self.test_time = datetime.now()
        self.test_time_iso = self.test_time.isoformat()
        self.test_id = str(uuid4())

    def test_init_no_kwargs(self):
        """Checks instance creation"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsNotNone(bm.id)
        self.assertIsNotNone(bm.created_at)
        self.assertIsNotNone(bm.updated_at)

    def test_init_kwargs(self):
        """Checks instance creation with kwargs"""
        bm = BaseModel(id=self.test_id, created_at=self.test_time_iso,
                       updated_at=self.test_time_iso)
        self.assertEqual(bm.id, self.test_id)
        self.assertEqual(bm.created_at, self.test_time)
        self.assertEqual(bm.updated_at, self.test_time)

    def test_uniq_id(self):
        """Checks if ids are unique"""
        bm = BaseModel()
        self.assertNotEqual(bm.id, self.test_bm.id)

    def test_save(self):
        """Test the save method of BaseModel"""
        bm = BaseModel()
        old_date = bm.updated_at
        time.sleep(0.3)
        bm.save()
        new_date = bm.updated_at
        self.assertNotEqual(new_date, old_date)
        with open("file.json", "r") as f:
            self.assertIn(bm.id, f.read())

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        bm = BaseModel()
        dico = bm.to_dict()
        self.assertIsInstance(dico, dict)
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        bm = BaseModel()
        test_str = "{} ({}) {}".format(
            bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(bm.__str__(), test_str)


if __name__ == "__main__":
    unittest.main()
