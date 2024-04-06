#!/usr/bin/python3

"""Test module for the Review class"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """Test case for the Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_type(self):
        """Test the type of the place_id attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.place_id), str)

    def test_user_id_type(self):
        """Test the type of the user_id attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.user_id), str)

    def test_text_type(self):
        """Test the type of the text attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.text), str)
