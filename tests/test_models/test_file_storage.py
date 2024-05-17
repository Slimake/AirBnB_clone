"""Unittest for FileStorage class"""

from models.engine.file_storage import FileStorage
from models import storage
import unittest


class TestFileStorage(unittest.TestCase):
    """Defines test for FileStorage class"""

    def setUp(self):
        """Declare a variable fs set to instance of FileStorage"""
        self.fs = FileStorage()

    def tearDown(self):
        """Delete fs variable"""
        del self.fs

    def test_file_storage_methods(self):
        """Test FileStorage class public methods"""
        self.assertIsInstance(self.fs.all(), dict)

    def test_storage_var(self):
        self.assertIsInstance(storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
