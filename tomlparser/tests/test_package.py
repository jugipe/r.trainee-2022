"""
Reaktor Fall 2022 Software developer trainee
Preliminary Assignment

This module has some unittests for the package module
"""
import unittest
from tomlparser.package import Package

class TestPackage(unittest.TestCase):
    p = Package("TestPackage")
    p.set_installed()

    p2 = Package("TestPackage2")
    p2.set_installed()

    p3 = Package("A_TestPackage")

    def test_Package_setters_and_getters(self):

        self.assertEqual(self.p.get_name(), "TestPackage")

        desc = "this is a test package"
        self.p.set_desc(desc)
        self.assertEqual(self.p.get_desc(), desc)

        self.assertTrue(self.p.get_installed())

        self.p.add_depency(self.p2)
        self.p.add_depency(self.p3)
        self.assertEqual(self.p.get_depencies(), [self.p3, self.p2])

        self.p.add_reverse_depency(self.p2)
        self.p.add_reverse_depency(self.p3)
        self.assertEqual(self.p.get_reverse_depencies(), [self.p3, self.p2])

if __name__ == "__main__":
    unittest.main()
