#!/usr/bin/python3
"""
test module for console.py
"""

import unittest
import cmd
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """testing the Console class."""

    def setUp(self):
        """unittest setup method"""
        self.test_c = HBNBCommand()

    def test_emptyline(self):
        """Checks empty line + ENTER"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_c.emptyline()
            self.assertEqual(f.getvalue(), "")
            self.assertEqual(self.test_c.prompt, "(hbnb) ")

    def test_do_EOF(self):
        """Checks EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.test_c.do_EOF("")
            self.assertEqual(f.getvalue(), "\n")
            self.assertEqual(self.test_c.prompt, "(hbnb) ")

    def test_do_quit(self):
        """Checks quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.test_c.do_quit("")


if __name__ == "__main__":
    unittest.main()
