#!/usr/bin/python3
"""
Unittest class module
Created on Monday 13.02.2023
@author: Rungene
"""

import unittest
from models.base_model import BaseModel
import inspect
import pep8


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
