#!/usr/bin/python3

"""Test module for the Amenity class"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenity(test_basemodel):
    """Test case for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_type(self):
        """Test the type of the name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
