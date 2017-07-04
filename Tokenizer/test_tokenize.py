import unittest
from unittest import TestCase

from PySearch.Tokenizer.tokenize import tokenize


class TestTokenize(TestCase):

    def test_tokenize_simple(self):
        self.assertEqual(tokenize("dette er en test"), ["dette", "er", "en", "test"])
        self.assertEqual(tokenize("hei"), ["hei"])
        self.assertEqual(tokenize(""), [])
        self.assertEqual(tokenize(" "), [])
        self.assertEqual(tokenize("     \n\t"), [])

    def test_tokenize_invalid_args(self):
        with self.assertRaises(AssertionError):
            tokenize(45)

    def test_tokenize_basic_seperation(self):
        self.assertEqual(tokenize("test(noe)"), ["test", "(", "noe", ")"])
        self.assertEqual(tokenize("test(noe!)"), ["test", "(", "noe!", ")"])
        self.assertEqual(tokenize("test.noe,hei."), ["test", ".", "noe", ",", "hei", "."])

    def test_tokenize_advanced_seperation(self):
        self.assertEqual(tokenize('"""test(noe)"""'), ['"""', 'test', '(', 'noe', ')', '"""'])



if __name__ == "__main__":
    unittest.main()
