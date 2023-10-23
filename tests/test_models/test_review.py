#!/usr/bin/python3
"""
TestFile for Review
"""

import unittest
from datetime import datetime as dt
from models.base_model import BaseModel
from models.review import Review


class TestBaseModel(unittest.TestCase):
    """Class defines Test file for BaseModel
    Inherits from unittest
    """

    def test_name(self):
        """Test name attribute type"""
        new = Review()
        new.name = "Kaicee"
        self.assertEqual(type(new.name), str)

    def test_instance(self):
        r = Review()
        self.assertIsInstance(Review, r)
        self.assertTrue(issubclass(type(r), BaseModel))

    def test_attr(self):
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))

    def test_Updated_at_type(self):
        """Test updated_at attribute type"""
        b = BaseModel()
        self.assertEqual(type(b.updated_at), type(dt.now()))

    def test_created_at_type(self):
        """Test created_at attribute type"""
        b = BaseModel()
        self.assertEqual(type(b.created_at), type(dt.now()))

    def test_id_type(self):
        """Test id attribute type"""
        b = BaseModel()
        self.assertEqual(type(b.id), str)

    def test_dict_id(self):
        """Test dictionary and instance id values"""
        b = BaseModel()
        my_dict = b.to_dict()
        self.assertEqual(b.id, my_dict['id'])

    def test_dict_updated_at(self):
        """Test updated_at dictionary attribute type"""
        b = BaseModel()
        my_dict = b.to_dict()
        self.assertEqual(b.updated_at.isoformat(), my_dict['updated_at'])

    def test_dict_created_at(self):
        """Test created_at dictionary atttribute type"""
        b = BaseModel()
        my_dict = b.to_dict()
        self.assertEqual(b.created_at.isoformat(), my_dict['created_at'])

    def test_class_name(self):
        """Test class_name value in dictionary"""
        b = BaseModel()
        my_dict = b.to_dict()
        self.assertEqual(type(b).__name__, my_dict['__class__'])

    def test_instance(self):
        """Test instance of class"""
        b = BaseModel()
        self.assertIsInstance(BaseModel(), type(b))

    def test_save_updated_at(self):
        """Test updated_at values after save()"""
        b = BaseModel()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertNotEqual(before['updated_at'], after['updated_at'])

    def test_save_created_at(self):
        """Test created_at values after save()"""
        b = BaseModel()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['created_at'], after['created_at'])

    def test_save_id(self):
        """Test id attribute value after save"""
        b = BaseModel()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['id'], after['id'])

    def test_dicttype_created_at(self):
        """Test created_at dictionary type"""
        b = BaseModel()
        my_dict = b.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))

    def test_dicttype_updated_at(self):
        """Test updated_at dictionary type"""
        b = BaseModel()
        my_dict = b.to_dict()
        self.assertEqual(str, type(my_dict['updated_at']))


if __name__ == "__main__":
    unittest.main()
