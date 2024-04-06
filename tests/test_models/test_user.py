#!/usr/bin/python3

"""Test module for the User class"""

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Test case for the User class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_type(self):
        """Test the type of the first_name attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.first_name), str)

    def test_last_name_type(self):
        """Test the type of the last_name attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.last_name), str)

    def test_email_type(self):
        """Test the type of the email attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.email), str)

    def test_password_type(self):
        """Test the type of the password attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.password), str)
