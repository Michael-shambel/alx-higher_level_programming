#!/usr/bin/python3
"""unitest for matrix"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -7]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 5, -3, 7]), 7)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)
if __name__ == '__main__':
    unittest.main()
