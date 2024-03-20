#!/usr/bin/python3
"""
program to test file Amenity.py
"""
import models
import unittest
from models.amenity import Amenity
class TestEmptyClassAttributeAmenity(unittest.TestCase):
    """
    class to test for empty attribute
    """
    def test_empty_attribute(self):
        """
        test for empty atribute
        """
        self.assertEqual(Amenity.name, "")
if __name__ == "__main__":
    unittest.main()

class TestSubclassAmenity(self):
    self.assertTrue(issubclass(amenity, console))





