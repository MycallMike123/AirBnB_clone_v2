#!/usr/bin/python3

"""Test module for the BaseModel class"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default_instance(self):
        """Test creating a default instance"""
        instance = self.value()
        self.assertEqual(type(instance), self.value)

    def test_kwargs_instance(self):
        """Test creating an instance with kwargs"""
        instance = self.value()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertFalse(new_instance is instance)

    def test_kwargs_int(self):
        """Test creating an instance with integer kwargs"""
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**copy)

    def test_save_method(self):
        """Test the save method"""
        instance = self.value()
        instance.save()
        key = self.name + "." + instance.id
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_to_string_method(self):
        """Test the __str__ method"""
        instance = self.value()
        expected_output = '[{}] ({}) {}'.format(self.name, instance.id,
                                                instance.__dict__)
        self.assertEqual(str(instance), expected_output)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        instance = self.value()
        self.assertEqual(instance.to_dict(), instance.to_dict())

    def test_kwargs_none(self):
        """Test creating an instance with None kwargs"""
        kwargs = {None: None}
        with self.assertRaises(TypeError):
            new_instance = self.value(**kwargs)

    def test_kwargs_one(self):
        """Test creating an instance with one kwargs"""
        kwargs = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new_instance = self.value(**kwargs)

    def test_id_type(self):
        """Test the type of the id attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.id), str)

    def test_created_at_type(self):
        """Test the type of the created_at attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.created_at), datetime.datetime)

    def test_updated_at_type(self):
        """Test the type of the updated_at attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.updated_at), datetime.datetime)
        instance_dict = new_instance.to_dict()
        new_instance = BaseModel(**instance_dict)
        self.assertFalse(new_instance.created_at == new_instance.updated_at)
