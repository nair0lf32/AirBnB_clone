#!/usr/bin/python3
"""
test module for models/review.py
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Testing the Review class"""

    def setUp(self):
        """unittest setup method"""
        self.test_bm = BaseModel()
        self.test_rv = Review()

    def test_no_args_instance(self):
        """Checks instance creation"""
        self.assertIsInstance(self.test_rv, Review)

    def test_args_instance(self):
        """Checks instantiation with args"""
        rv = Review(place_id="69", user_id="69", text="test")
        self.assertIsInstance(rv, Review)
        self.assertEqual(str, type(rv.text))
        self.assertEqual("test", rv.text)
        self.assertEqual(str, type(rv.place_id))
        self.assertEqual("69", rv.place_id)
        self.assertEqual(str, type(rv.user_id))
        self.assertEqual("69", rv.user_id)
