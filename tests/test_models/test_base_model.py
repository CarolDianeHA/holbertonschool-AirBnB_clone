import unittest
from models.base_model import BaseModel
import models
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        model = BaseModel()
        expected_output = "[{}] ({}) {}".format(
            model.__class__.__name__, model.id, model.__dict__)
        self.assertEqual(str(model), expected_output)

    def test_save(self):
        model = BaseModel()
        prev_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, prev_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.fromisoformat(
            model_dict['created_at']), datetime)
        self.assertIsInstance(datetime.fromisoformat(
            model_dict['updated_at']), datetime)


if __name__ == '__main__':
    unittest.main()
