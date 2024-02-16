#!/usr/bin/python3
""" Unittests cases for base_model """

import time
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """ Test case for User class
    """
    def setUp(self):
        """ Run before every single test
        """
        self.model = BaseModel()

    def tearDown(self):
        """ Run after every single test
        """
        pass

    def test_attr(self):
        """ Test Class attributes
        """
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        # Check Datatype
        model_2 = BaseModel()
        # Check that id is unique
        self.assertNotEqual(self.model.id, model_2.id)
        self.assertEqual(type(self.model.id), str)
        self.assertEqual(type(self.model.created_at), datetime)
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_inheritance(self):
        """ Test inheritance from BaseModel
        """
        self.assertIsInstance(self.model, BaseModel)

    def test_str(self):
        """ Test string representation of Basemodel
        """
        self.assertIsInstance(str(self.model), str)

    def test_to_dict(self):
        """ Test to_dict method
        """
        self.model.name = "James"
        self.model.phone = "+1 555 2345"
        m_d = self.model.to_dict()  # Model_dict
        self.assertEqual(m_d["id"], self.model.id)
        self.assertEqual(m_d["created_at"], self.model.created_at.isoformat())
        self.assertEqual(m_d["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(m_d["__class__"], type(self.model).__name__)
        self.assertEqual(m_d["name"], self.model.name)
        self.assertEqual(m_d["phone"], self.model.phone)

    def test_save(self):
        """ Test Save method
        """
        model_2 = BaseModel()
        time.sleep(0.3)
        now = datetime.now()
        model_2.save()
        latency = model_2.updated_at - now
        self.assertTrue(abs(latency.total_seconds()) < 0.01)


# Run as main file if called
if __name__ == "__main__":
    unittest.main()
