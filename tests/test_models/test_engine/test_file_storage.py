#!/usr/bin/python3

"""Module for testing file storage"""

import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Class to test the file storage method"""

    def setUp(self):
        """Set up test environment"""
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Remove storage file at the end of tests"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """Check if __objects is initially empty"""
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """Test if a new object is correctly added to __objects"""
        new_obj = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """Test if __objects is properly returned"""
        new_obj = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """Check if a file is not created on BaseModel save"""
        new_obj = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """Test if data is saved to file"""
        new_obj = BaseModel()
        data = new_obj.to_dict()
        new_obj.save()
        new_obj_2 = BaseModel(**data)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """Test the FileStorage save method"""
        new_obj = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """Test if the storage file is successfully loaded to __objects"""
        new_obj = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new_obj.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """Test reloading from an empty file"""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Test that nothing happens if the file does not exist"""
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """Test if the BaseModel save method calls storage save"""
        new_obj = BaseModel()
        new_obj.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """Confirm that __file_path is a string"""
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm that __objects is a dictionary"""
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """Test if the key is properly formatted"""
        new_obj = BaseModel()
        _id = new_obj.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """Test if the FileStorage object 'storage' is created"""
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
