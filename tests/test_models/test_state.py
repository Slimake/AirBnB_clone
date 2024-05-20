"""Unittest for Review class"""

from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Defines test for State class"""

    def setUp(self):
        """Declare a variable state set to the instance of State classs"""
        self.state = State()

    def tearDown(self):
        """Delete state variable"""
        del self.state

    def test_name_attr(self):
        """Test for name attribute of State class"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(type(self.state.name), str)


if __name__ == "__main__":
    unittest.main()
