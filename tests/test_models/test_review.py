#!/usr/bin/python3
"""
program used to test for file review.py
"""
import models
import unittest
from models.review import Review
class TestEmptyAttributeReview(unittest.TestCase):
    """
    class used to test for empty class attributes
    """
    def test_empty_class_attribute(self):
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

if __name__ == "__main__":
    unittest.main()


