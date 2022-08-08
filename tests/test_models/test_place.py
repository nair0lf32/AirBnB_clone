#!/usr/bin/python3
"""
test module for models/place.py
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Testing the Place class"""

    def setUp(self):
        """unittest setup method"""
        self.test_bm = BaseModel()
        self.test_pl = Place()

    def test_no_args_instance(self):
        """Checks instance creation"""
        self.assertIsInstance(self.test_pl, Place)

    def test_args_instance(self):
        """Checks instantiation with args"""
        pl = Place(city_id="69", user_id="420", name="test")
        self.assertIsInstance(pl, Place)
        self.assertEqual(str, type(pl.name))
        self.assertEqual("test", pl.name)
        self.assertEqual(str, type(pl.city_id))
        self.assertEqual("69", pl.city_id)
        self.assertEqual(str, type(pl.user_id))
        self.assertEqual("420", pl.user_id)
        pl.description = "test description"
        self.assertEqual(str, type(pl.description))
        self.assertEqual("test description", pl.description)
        pl.number_rooms = 1
        self.assertEqual(int, type(pl.number_rooms))
        self.assertEqual(1, pl.number_rooms)
        pl.number_bathrooms = 1
        self.assertEqual(int, type(pl.number_bathrooms))
        self.assertEqual(1, pl.number_bathrooms)
        pl.max_guest = 1
        self.assertEqual(int, type(pl.max_guest))
        self.assertEqual(1, pl.max_guest)
        pl.price_by_night = 1
        self.assertEqual(int, type(pl.price_by_night))
        self.assertEqual(1, pl.price_by_night)
        pl.latitude = 1.0
        self.assertEqual(float, type(pl.latitude))
        self.assertEqual(1.0, pl.latitude)
        pl.longitude = 1.0
        self.assertEqual(float, type(pl.longitude))
        self.assertEqual(1.0, pl.longitude)
        pl.amenity_ids = ["1", "2"]
        self.assertEqual(list, type(pl.amenity_ids))
        self.assertEqual(["1", "2"], pl.amenity_ids)
