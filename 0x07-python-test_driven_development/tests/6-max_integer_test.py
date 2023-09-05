import unittest

max_integer = __import__('6-max_integer').max_integer

class MaxInteger(unittest.TestCase):
    """MaxInteger - a unittest type class to run test on 6-max_integer module"""
    def test_listlen(self):
        """test for list length"""
        self.assertEqual(max_integer([]), None)
