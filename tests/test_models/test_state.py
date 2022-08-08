#!/usr/bin/python3
"""
test module for models/state.py
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class Teststate(unittest.TestCase):
    """Testing the State class"""

    def setUp(self):
        """unittest setup method"""
        self.test_bm = BaseModel()
        self.test_st = State()

    def test_no_args_instance(self):
        """Checks instance creation"""
        self.assertIsInstance(self.test_st, State)

    def test_args_instance(self):
        """Checks instantiation with args"""
        st = State(name="test")
        self.assertIsInstance(st, State)
        self.assertEqual(str, type(st.name))
        self.assertEqual("test", st.name)
