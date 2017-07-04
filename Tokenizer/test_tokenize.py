import unittest
from unittest import TestCase

from PySearch.Tokenizer.tokenize import tokenize


class TestTokenize(TestCase):

    def test_tokenize(self):
        self.assertEqual(tokenize("dette er en test"), ["dette", "er", "en", "test"])



if __name__ == "__main__":
    unittest.main()
