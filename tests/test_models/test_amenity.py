#!/usr/bin/python3
"""
test module for models/amenity.py
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Testing the Amenity class"""

    def setUp(self):
        """unittest setup method"""
        self.test_bm = BaseModel()
        self.test_am = Amenity()

    def test_no_args_instance(self):
        """Checks instance creation"""
        self.assertIsInstance(self.test_am, Amenity)

    def test_args_instance(self):
        """Checks instantiation with args"""
        am = Amenity(name="test")
        self.assertIsInstance(am, Amenity)
        self.assertEqual(str, type(am.name))
        self.assertEqual("test", am.name)
