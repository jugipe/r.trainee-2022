import unittest
import Parser

class TestParser(unittest.TestCase):
    
    def test_known_project(self):
        parsed = Parser.TOML_Parser("testpoetry.lock")

        self.assertEqual(dict, type(parsed.get_data()))

        self.assertEqual("click", parsed.get_data()["click"].get_name())

        self.assertEqual(9, len(parsed.get_data()))


    def test_empty_project(self):
        parsed = Parser.TOML_Parser("testempty.lock")

        self.assertEqual(0, len(parsed.get_data()))


if __name__ == "__main__":
    unittest.main()