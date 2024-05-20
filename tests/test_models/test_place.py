"""Unittest for Place class"""

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Defines test for Place class"""

    def setUp(self):
        """Declare a variable Place set to the instance of Place classs"""
        self.place = Place()

    def tearDown(self):
        """Delete place variable"""
        del self.place

    def test_amenity_ids_attr(self):
        """Test the amenity_ids attribute of Place class"""
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_city_id_attr(self):
        """Test the city_id attribute of Place class"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(type(self.place.city_id), str)

    def test_description_attr(self):
        """Test the description attribute of Place class"""
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(type(self.place.description), int)

    def test_latitude_attr(self):
        """Test the latitude attribute of Place class"""
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(type(self.place.latitude), float)

    def test_longitude_attr(self):
        """Test the longitude attribute of Place class"""
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(type(self.place.longitude), float)

    def test_max_guest_attr(self):
        """Test the max_guest attribute of Place class"""
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(type(self.place.max_guest), int)

    def test_name_attr(self):
        """Test for name attribute of Place class"""
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(type(self.place.name), str)

    def test_number_bathrooms_attr(self):
        """Test the number_bathrooms attribute of Place class"""
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(type(self.place.number_bathrooms), int)

    def test_number_rooms_attr(self):
        """Test the number_rooms attribute of Place class"""
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(type(self.place.number_rooms), int)

    def test_price_by_night_attr(self):
        """Test the price_by_night attribute of Place class"""
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(type(self.place.price_by_night), int)

    def test_user_id_attr(self):
        """Test the user_id attribute of Place class"""
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(type(self.place.user_id), str)


if __name__ == "__main__":
    unittest.main()
