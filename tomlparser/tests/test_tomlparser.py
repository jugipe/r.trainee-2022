"""
Reaktor Fall 2022 Software developer trainee
Preliminary Assignment

This module has some unittests for the tomlparser module
"""
import unittest
import os
from tomlparser.tomlparser import TomlParser


class TestParser(unittest.TestCase):
    
    def test_known_project(self):
        test_filename = os.path.join(os.path.dirname(__file__), "testpoetry.lock")

        parsed = TomlParser(test_filename)

        self.assertEqual(dict, type(parsed.get_data()))

        self.assertEqual("click", parsed.get_data()["click"].get_name())

        self.assertEqual(9, len(parsed.get_data()))


    def test_empty_project(self):
        test_filename = os.path.join(os.path.dirname(__file__), "testempty.lock")
        
        parsed = TomlParser(test_filename)

        self.assertEqual(0, len(parsed.get_data()))


if __name__ == "__main__":
    unittest.main()