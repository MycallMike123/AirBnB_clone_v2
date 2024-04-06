#!/usr/bin/python3

"""Test module for the City class"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(test_basemodel):
    """Test case for the City class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_type(self):
        """Test the type of the state_id attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.state_id), str)

    def test_name_type(self):
        """Test the type of the name attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.name), str)
