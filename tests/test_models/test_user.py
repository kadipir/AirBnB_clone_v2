
#!/usr/bin/python3
"""test program on the user program
"""
import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel
class test_user(unittest.TestCase):
    def setUp(self):
        #temporary file for saving test data
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        #remove fike after test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attr(self):
        #create new user instance
        test_user = User()
        #check if the class atttr are empty
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inherits_from_BaseModel(self):
        test_user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        test_user = User()
        test_user.email = "john@gmail.com"
        test_user.first_name = "John"
        test_user.last_name = "Tim"
        test_user.password = "root"
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("john@gmail.com", user_str)
        self.assertIn("John", user_str)
        self.assertIn("Tim", user_str)
        self.assertIn("root", user_str)

    def test_user_to_dict(self):
        test_user = User()
        test_user.email = "john@gmail.com"
        test_user.first_name = "John"
        test_user.last_name = "Tim"
        test_user.password = "root"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict["email"], "john@gmail.com")
        self.assertEqual(user_dict["password"], "root")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Tim")

    def test_user_instance_creation(self):
        test_user = User(email = "john@gmail.com" ,first_name = "John", last_name = "Tim", password = "root")
        self.assertEqual(test_user.email, "john@gmail.com")
        self.assertEqual(test_user.password, "root")
        self.assertEqual(test_user.first_name,"John")
        self.assertEqual(test_user.last_name, "Tim")

    def test_user_instance_to_dict(self):
        test_user = User(email = "john@gmail.com" ,first_name = "John", last_name = "Tim", password = "root")
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict["email"], "john@gmail.com")
        self.assertEqual(user_dict["password"], "root")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Tim")

    def test_user_id_generation(self):
        test_user = User()
        user2 = User()
        self.assertNotEqual(test_user.id, user2.id)
if __name__ == "__main__":
    unittest.main()






   

        


