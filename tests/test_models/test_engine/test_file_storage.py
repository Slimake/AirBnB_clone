#!/usr/bin/python3
"""
Test file for class FileStorage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Class test for FileStorage using unit test"""
    def test_Objects_type(self):
        b = BaseModel()
        all_objs = storage.all()
        self.assertTrue(type(all_objs), dict)

    def test_key(self):
        """Tests the key of file_objects"""
        b = BaseModel()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            key = obj_id
        self.assertEqual(key, f"{type(b).__name__}.{b.id}")

    def test_obj(self):
        """Tests the value of file_objects"""
        b = BaseModel()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        self.assertIsInstance(obj, BaseModel)

    def test_save(self):
        """Tests the save method of FileStorage class"""
        b = BaseModel()
        before = b.updated_at
        b.save()
        after = b.updated_at
        self.assertNotEqual(before, after)

    def test_reload(self):
        """Tests the save method of FileStorage class"""
        b = BaseModel()
        b.save()
        storage.reload()
        b_key = f"{type(b).__name__}.{b.id}"
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id == b_key:
                obj = all_objs[obj_id]
        self.assertEqual(obj.updated_at, b.updated_at)


if __name__ == "__main__":
    unittest.main()
