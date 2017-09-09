import unittest
from unittest import TestCase

from PySearch.Search.boolean_search import search

class TestSearch(TestCase):

    def test_search_single_word(self):
        self.assertEqual(search("kaffe"), ["/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil1.txt"])
        self.assertEqual(search(""), [])
        self.assertEqual(search("dette"), ['/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil1.txt', '/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil2.txt', '/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil3.txt'])

    def test_search_mult_word(self):
        self.assertEqual(search("dette kaffe"), ["/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil1.txt"])
        self.assertEqual(search("kaffe sommer"), [])


if __name__ == "__main__":
    unittest.main()