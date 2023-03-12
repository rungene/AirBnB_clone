#!/usr/bin/python3
"""
Unittest class module
Created on Monday 13.02.2023
@author: Rungene
"""

import unittest
import os
from models.base_model import BaseModel
import inspect
import pep8
from datetime import datetime
import sys
sys.path.append('.')


class TestBaseModel(unittest.TestCase):
    """"
    TestBaseModel - class for testing BaseModel class methods
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(BaseModel, inspect.isfunction)

    def setUp(self):
        """
        Set up method for creating and object BM of BaseModel
        run before each test method.
        """
        self.BM = BaseModel()

    def tearDown(self):
        """
        setting the temp object to None
        run after each test
        """
        self.BM = None

    def test_basemodel_conform_pep8(self):
        """
        Test base_model.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_classbasetest_conform_pep8(self):
        """
        Test test_base.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(
                 ['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_basemodule_docstring(self):
        """
        tests if base module doc string exists
        """
        # doc = __import__('models/base').__doc__
        self.assertTrue(len('models/base_model.py'.__doc__) >= 1)

    def test_class_docstring(self):
        """
        test if class dosctring exists
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_method_docstring(self):
        """
        test if method docsting exists
        """
        for doc_mthd in self.setup:
            self.assertTrue(len(doc_mthd[1].__doc__) >= 1)

    def test_type_basemodel(self):
        """
        test if Basemodel type
        """
        self.assertIsInstance(self.BM, BaseModel)
        self.assertEqual(type(self.BM), BaseModel)

    def test_basic_attributes_areset(self):
        """test for proper assignment
        for attributes(basic)
        """
        self.BM.f_name = "Rungene"
        self.BM.l_name = "Lawrence"
        self.assertEqual(self.BM.f_name, "Rungene")
        self.assertEqual(self.BM.l_name, "Lawrence")

    def test_str(self):
        """test str method
        """
        string = str(self.BM)
        BMstr = "[{}] ({}) {}".format(self.BM.__class__.__name__, self.BM.id,
                                      self.BM.__dict__)
        test_val = BMstr in string
        self.assertEqual(True, test_val)
        test_val = 'updated_at' in string
        self.assertEqual(True, test_val)
        tet_val = 'created_at' in string
        self.assertEqual(True, test_val)
        test_val = 'datetime' in string
        self.assertEqual(True, test_val)

    def test_to_dict(self):
        """test to_dict method
        """
        my_dict = self.BM.to_dict()
        self.assertEqual(str, type(my_dict['created_at']))
        self.assertEqual(my_dict['created_at'],
                         self.BM.created_at.isoformat())
        self.assertEqual(datetime, type(self.BM.created_at))
        self.assertEqual(my_dict['__class__'],
                         self.BM.__class__.__name__)
        self.assertEqual(my_dict['id'], self.BM.id)

    def test_to_dict_more(self):
        """more test to_dict method
        """
        my_dict = self.BM.to_dict()
        created_at = my_dict['created_at']
        time = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(self.BM.created_at, time)

    def test_from_dict_basic(self):
        """test from dictonary to object
        """
        my_dict = self.BM.to_dict()
        BM1 = BaseModel(**my_dict)
        self.assertEqual(BM1.id, self.BM.id)
        self.assertEqual(BM1.updated_at, self.BM.updated_at.isoformat())
        self.assertEqual(BM1.created_at, self.BM.created_at.isoformat())
        self.assertEqual(BM1.__class__.__name__,
                         self.BM.__class__.__name__)


if __name__ == "__main__":
    unittest.main()
