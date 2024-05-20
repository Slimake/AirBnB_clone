"""Unittest for City class"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Defines test for City class"""

    def setUp(self):
        """Declare a variable city set to the instance of City classs"""
        self.city = City()

    def tearDown(self):
        """Delete city variable"""
        del self.city

    def test_name_attr(self):
        """Test for name attribute of City class"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(type(self.city.name), str)

    def test_state_id_attr(self):
        """Test the state_id attribute of City class"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(type(self.city.state_id), str)


if __name__ == "__main__":
    unittest.main()
