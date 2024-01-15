#!/usr/bin/python3
"""define unittest for base for every class"""
import os
import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    """unittest for base classes:
    this going to test creating base 
    save the string and test jsom string"""

    def test_init_with_id(self):
        instance = Base(id=5)
        self.assertEqual(instance.id, 5)

    def test_init_without_id(self):
        instance1 = Base()
        instance2 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
