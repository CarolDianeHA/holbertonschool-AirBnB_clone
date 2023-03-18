import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.bm1 = BaseModel()
        self.am1 = Amenity()
        self.ct1 = City()
        self.pl1 = Place()
        self.st1 = State()
        self.ur1 = User()
        self.rv1 = Review()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(type(self.storage.all()), dict)
        self.assertIn('BaseModel.' + self.bm1.id, self.storage.all())

    def test_new(self):
        self.storage.new(self.am1)
        key = 'Amenity.' + self.am1.id
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_save_reload(self):
        self.storage.new(self.ct1)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = 'City.' + self.ct1.id
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
