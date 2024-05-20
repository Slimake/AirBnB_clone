"""Unittest for Amenity class"""

from models.amenity import Amenity
import unittest

class TestAmenityClass(unittest.TestCase):
    """Defines test for Amenity class"""

    def test_name(self):
        """Test the name attribute of the amenity class"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(type(amenity.name), str)

if __name__ == "__main__":
    unittest.main()