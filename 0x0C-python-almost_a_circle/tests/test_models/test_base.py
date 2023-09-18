#!/usr/bin/python3

import unittest
import inspect
import importlib

# Import your module dynamically
module = importlib.import_module('models.base')

class TestDocstrings(unittest.TestCase):

    def test_module_docstring(self):
        """
        Test the docstring for the module (models.base).
        """
        self.assertIsNotNone(module.__doc__, "Module docstring is missing.")
        self.assertNotEqual(len(module.__doc__.strip()), 0, "Module docstring is empty.")

    def test_class_docstring(self):
        """
        Test the docstring for the class inside the module.
        """
        Base = getattr(module, 'Base', None)
        self.assertIsNotNone(Base, "Class not found in the module.")
        self.assertIsNotNone(Base.__doc__, "Class docstring is missing.")
        self.assertNotEqual(len(Base.__doc__.strip()), 0, "Class docstring is empty.")

    def test_function_docstrings(self):
        """
        Test the docstrings for functions inside the class.
        """
        Base = getattr(module, 'Base', None)
        self.assertIsNotNone(Base, "Class not found in the module.")

        # Replace 'save_to_file', 'from_json_string', etc., with the actual function names
        functions_to_test = ['save_to_file', 'from_json_string']

        for func_name in functions_to_test:
            func = getattr(Base, func_name, None)
            self.assertIsNotNone(func, f"Function '{func_name}' not found in the class.")
            self.assertIsNotNone(func.__doc__, f"Docstring for function '{func_name}' is missing.")
            self.assertNotEqual(len(func.__doc__.strip()), 0, f"Docstring for function '{func_name}' is empty.")

if __name__ == '__main__':
    unittest.main()
