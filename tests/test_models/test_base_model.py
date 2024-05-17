"""Unittest for BaseModel class"""

from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Defines test for BaseModel class"""

    def setUp(self):
        """Declare a variable basemodel set to instance of BaseModel"""
        self.basemodel1 = BaseModel()
        self.basemodel2 = BaseModel()
        self.basemodel2.number = 4
        self.dic = self.basemodel2.to_dict()

    def tearDown(self):
        """Delete basemodel variable"""
        del self.basemodel1
        del self.basemodel2
        del self.dic

    """Defines TestBaseModel class"""
    def test_instance_attr(self):
        """Test instance attributes of BaseModel class"""
        self.assertTrue(hasattr(self.basemodel1, "id"))
        self.assertTrue(hasattr(self.basemodel1, "created_at"))
        self.assertTrue(hasattr(self.basemodel1, "updated_at"))
        self.assertTrue(hasattr(self.basemodel1, "save"))
        self.assertTrue(hasattr(self.basemodel1, "to_dict"))

    def test_instance(self):
        """Test instance of BaseModel class and its attributes"""
        self.assertIsInstance(self.basemodel2, BaseModel)
        self.assertIsInstance(self.basemodel2.id, str)
        self.assertIsInstance(self.basemodel2.number, int)
        self.assertIsInstance(self.basemodel2.created_at, datetime)
        self.assertIsInstance(self.basemodel2.updated_at, datetime)

    def test_to_dict_dictionary(self):
        """Test to_dict dictionary keys"""
        self.assertIsInstance(self.dic['id'], str)
        self.assertIsInstance(self.dic['number'], int)
        self.assertIsInstance(self.dic['created_at'], str)
        self.assertIsInstance(self.dic['updated_at'], str)

    def test_save_updated_at_equality(self):
        """Test save method"""
        before_save = self.basemodel1.updated_at
        self.assertIs(self.basemodel1.updated_at, self.basemodel1.updated_at)
        self.basemodel1.save()
        self.assertIsNot(before_save, self.basemodel1.updated_at)

    def test_instance_equality(self):
        """Test instance of BaseModel class"""
        self.assertIs(self.basemodel1, self.basemodel1)
        self.assertIsNot(self.basemodel1, self.basemodel2)


if __name__ == "__main__":
    unittest.main()
