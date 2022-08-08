#!/usr/bin/python3
"""
test module for models/city.py
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Testing the City class"""

    def setUp(self):
        """unittest setup method"""
        self.test_bm = BaseModel()
        self.test_ct = City()

    def test_no_args_instance(self):
        """Checks instance creation"""
        self.assertIsInstance(self.test_ct, City)

    def test_args_instance(self):
        """Checks instantiation with args"""
        ct = City(state_id="69", name="test")
        self.assertIsInstance(ct, City)
        self.assertEqual(str, type(ct.name))
        self.assertEqual("test", ct.name)
        self.assertEqual(str, type(ct.state_id))
        self.assertEqual("69", ct.state_id)
