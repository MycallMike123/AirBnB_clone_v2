#!/usr/bin/python3

"""Test module for the Place class"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """Test case for the Place class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id_type(self):
        """Test the type of the city_id attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.city_id), str)

    def test_user_id_type(self):
        """Test the type of the user_id attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.user_id), str)

    def test_name_type(self):
        """Test the type of the name attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.name), str)

    def test_description_type(self):
        """Test the type of the description attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.description), str)

    def test_number_rooms_type(self):
        """Test the type of the number_rooms attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.number_rooms), int)

    def test_number_bathrooms_type(self):
        """Test the type of the number_bathrooms attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.number_bathrooms), int)

    def test_max_guest_type(self):
        """Test the type of the max_guest attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.max_guest), int)

    def test_price_by_night_type(self):
        """Test the type of the price_by_night attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.price_by_night), int)

    def test_latitude_type(self):
        """Test the type of the latitude attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.latitude), float)

    def test_longitude_type(self):
        """Test the type of the longitude attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.longitude), float)

    def test_amenity_ids_type(self):
        """Test the type of the amenity_ids attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.amenity_ids), list)
