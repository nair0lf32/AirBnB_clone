#!/usr/bin/python3
"""
test module for models/user.py
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class Testuser(unittest.TestCase):
    """Testing the User class"""

    def setUp(self):
        """unittest setup method"""
        self.test_bm = BaseModel()
        self.test_u = User()

    def test_no_args_instance(self):
        """Checks instance creation"""
        self.assertIsInstance(self.test_u, User)

    def test_args_instance(self):
        """Checks instantiation with args"""
        u = User(email="test@mail.com", password="test123")
        self.assertIsInstance(u, User)
        self.assertEqual(str, type(u.email))
        self.assertEqual("test@mail.com", u.email)
        self.assertEqual(str, type(u.password))
        self.assertEqual("test123", u.password)
        u.first_name = "joe"
        self.assertEqual(str, type(u.first_name))
        self.assertEqual("joe", u.first_name)
        u.last_name = "mama"
        self.assertEqual(str, type(u.last_name))
        self.assertEqual("mama", u.last_name)
