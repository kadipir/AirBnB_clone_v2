#!/usr/bin/python3
"""
program to test for the file state.py 
"""
import models
import unittest
from models.state import State
class TestState(unittest.TestCase):
    """
    test for empty string
    """
    def test_empty_string(self):
        self.assertEqual(State.name, "")
if __name__ == "__main__":
    unittest.main()
