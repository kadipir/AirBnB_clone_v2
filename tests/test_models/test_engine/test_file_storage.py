#!/usr/bin/python3
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstantiation(unittest.TestCase):
    """
    testing the instantiation of the file storage
    """
    def test_FileStorage_instantiation_noArgs(self):
        """test FileStorage with arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)
        """FileStorage with no arguments"""
    def test_FileStorage_instantiation_withArgs(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
    def test_storage_initialization(self):
        """test the initialization of storage as an instance of FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)
class test_FileStorage(unittest.TestCase):
    """test of the attriutes pof the class FileStorage"""
    def setUp(self):
        """create a  storage json file that is temporary"""
        self.test_file = "test_file.json"
    def del_setUp_file(self):
        """delete temporary file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    def test_all_dictionary(self):
        """test if all attribute returns a dictionary"""
        self.assertEqual(dict,type(models.storage.all()))
    def test_new(self):
        """test for creation and storing new objects"""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id),models.storage.all())
    def test_save_and_reload(self):  
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()
        #create new storage to simulate reloading"""
        new_storage = FileStorage()
        new_storage.reload()
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)
    def test_save_to_file(self):
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))
if __name__ == "__main__":
    unittest.main











