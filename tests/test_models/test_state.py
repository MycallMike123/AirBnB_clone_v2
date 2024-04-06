#!/usr/bin/python3

"""Test module for the State class"""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """Test case for the State class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """Test the type of the name attribute"""
        new_instance = self.value()
        self.assertEqual(type(new_instance.name), str)
