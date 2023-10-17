#!/usr/bin/python3
"""
TestFile for class Review
"""

import unittest
from datetime import datetime as dt
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class defines Test file for Review
    Inherits from BaseModel
    """

    def test_place_id(self):
        """Test name attribute type"""
        new = Review()
        new.place_id = "234234324"
        self.assertEqual(type(new.place_id), str)

    def test_text(self):
        """Test password attribute type"""
        new = Review()
        new.text = "Nice comfortable home"
        self.assertEqual(type(new.text), str)

    def test_Updated_at_type(self):
        """Test updated_at attribu8te type"""
        n = Review()
        self.assertEqual(type(n.updated_at), type(dt.now()))

    def test_id_type(self):
        """Test id attribute Type"""
        n = Review()
        self.assertEqual(type(n.id), str)

    def test_dict_id(self):
        """Test id attribute uniquness in saved dict"""
        b = Review()
        my_dict = b.to_dict()
        self.assertEqual(b.id, my_dict['id'])

    def test_dict_created_at(self):
        """Test created_at attribute type in dictionary"""
        b = Review()
        my_dict = b.to_dict()
        self.assertEqual(b.updated_at.isoformat(), my_dict['updated_at'])

    def test_class_name(self):
        """Test class_name value in dictionary and instance"""
        b = Review()
        my_dict = b.to_dict()
        self.assertEqual(type(b).__name__, my_dict['__class__'])

    def test_instance(self):
        """Test instance of class"""
        b = Review()
        self.assertIsInstance(Review(), type(b))

    def test_save_updated_at(self):
        """Test updated_at variable after save() is called"""
        b = Review()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertNotEqual(before['updated_at'], after['updated_at'])

    def test_save_created_at(self):
        """Test created_at variable after save() is called"""
        b = Review()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['created_at'], after['created_at'])

    def test_save_id(self):
        """Test id uniqueness after save() is called"""
        b = Review()
        before = b.to_dict()
        b.save()
        after = b.to_dict()
        self.assertEqual(before['id'], after['id'])


if __name__ == "__main__":
    unittest.main()
