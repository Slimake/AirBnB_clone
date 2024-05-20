"""Unittest for Review class"""

from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Defines test for Review class"""

    def setUp(self):
        """Declare a variable review set to the instance of Review classs"""
        self.review = Review()

    def tearDown(self):
        """Delete review variable"""
        del self.review

    def test_place_id(self):
        """Test the place_id attribute of Place class"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(type(self.review.place_id), str)

    def test_text(self):
        """Test for text attribute of Review class"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(type(self.review.text), str)

    def test_user_id(self):
        """Test the user_id attribute of Review class"""
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(type(self.review.user_id), str)


if __name__ == "__main__":
    unittest.main()
