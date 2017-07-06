"""

 __author__ = hjenvild@gmail.com, arildlil@protonmail.com
"""


import unittest
from unittest import TestCase

from PySearch.Tokenizer.tokenize import tokenize


class TestTokenize(TestCase):

    def test_simple(self):
        self.assertEqual(tokenize("dette er en test"), ["dette", "er", "en", "test"])
        self.assertEqual(tokenize("hei"), ["hei"])

    def test_none_line(self):
        self.assertEqual(tokenize(""), [])
        self.assertEqual(tokenize(" "), [])
        self.assertEqual(tokenize("     \n\t"), [])

    def test_invalid_args(self):
        with self.assertRaises(AssertionError):
            tokenize(45)

    def test_basic_separation(self):
        self.assertEqual(tokenize("test(noe)"), ["test", "(", "noe", ")"])
        self.assertEqual(tokenize("test(noe!)"), ["test", "(", "noe","!", ")"])
        self.assertEqual(tokenize("test.noe,hei."), ["test", ".", "noe", ",", "hei", "."])

    def test_advanced_seperation(self):
        self.assertEqual(tokenize('"""test(noe)"""'), ['"', '"', '"', 'test', '(', 'noe', ')', '"', '"', '"'])


if __name__ == "__main__":
    unittest.main()
