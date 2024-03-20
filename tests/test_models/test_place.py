#!/usr/bin/python3
"""
program to test file place.py
"""
import models
import unittest
from models.place import Place

class TestEmptyAttributePlace(unittest.TestCase):
    """
    class to test for empty attribute

    """
    def test_empty_attribute_place(self):
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description,"")
        self.assertEqual(Place.amenity_ids, [])
    def test_data_type_of_attribute(self):
        """
        method to test for the data type of attribute of data values
        """
        self.assertIsInstance(Place.number_rooms,int)
        self.assertIsInstance(Place.number_bathrooms,int)
        self.assertIsInstance(Place.max_guest,int)
        self.assertIsInstance(Place.price_by_night,int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude,float)


if __name__ == "__main__":
    unittest.main()




