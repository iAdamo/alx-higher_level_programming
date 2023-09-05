#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

"""Unittests for max_integer() function using TestMaxinteger class
TestMaxInteger is a subclass of unittest.Testcase"""


class TestMaxInteger(unittest.TestCase):
    """ MaxInteger - a unittest type class to run test on 6-max_integer module"""
    def test_empty_list(self):
        """Test when input list is empty."""
        self.assertEqual(max_integer([]), None)

    def test_positive_numbers(self):
        """Test when input list contains positive numbers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test when input list contains negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """Test when input list contains a mix of negative, zero, and positive numbers."""
        self.assertEqual(max_integer([-1, 0, 1, 2, 3]), 3)

    def test_duplicate_numbers(self):
        """Test when input list contains duplicate numbers."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_single_element(self):
        """Test when input list contains a single element."""
        self.assertEqual(max_integer([42]), 42)

    def test_sorted_list(self):
        """Test when input list is sorted in ascending order."""
        sorted_list = [2, 3, 4, 5]
        self.assertEqual(max_integer(sorted_list), 5)

    def test_unsorted_list(self):
        """Test when input list is unsorted."""
        unsorted_list = [5, 2, 4, 3]
        self.assertEqual(max_integer(unsorted_list), 5)

    def test_single_element_list(self):
        """Test when input list contains a single element."""
        single_elem_list = [3]
        self.assertEqual(max_integer(single_elem_list), 3)

    def test_float(self):
        """Test when input list contains all float values."""
        float_list = [2.85, 3.40, -8.103, 21.24, 9.0]
        self.assertEqual(max_integer(float_list), 21.24)

    def test_combination(self):
        """Test when input list contains a combination of integers and floats."""
        comb_list = [2.53, 18.5, -9, 15, 5]
        self.assertEqual(max_integer(comb_list), 18.5)

    def test_single_string(self):
        """Test when input is a single string."""
        string = "A sample string"
        self.assertEqual(max_integer(string), 't')

    def test_list_of_strings(self):
        """Test when input is a list of strings."""
        strings = ["Here", "to", "test", "this"]
        self.assertEqual(max_integer(strings), "to")

    def test_empty_string(self):
        """Test when input is an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
