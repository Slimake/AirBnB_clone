"""Unittest for Review class"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Defines test for User class"""

    def setUp(self):
        """Declare a variable user set to the instance of User classs"""
        self.user = User()

    def tearDown(self):
        """Delete user variable"""
        del self.user

    def test_email_attr(self):
        """Test the email attribute of User class"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(type(self.user.email), str)

    def test_first_name_attr(self):
        """Test for first_name attribute of User class"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name_attr(self):
        """Test for last_name attribute of User class"""
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(type(self.user.last_name), str)

    def test_password_attr(self):
        """Test the password attribute of User class"""
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(type(self.user.password), str)


if __name__ == "__main__":
    unittest.main()
