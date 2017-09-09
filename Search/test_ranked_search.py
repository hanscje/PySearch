import unittest
from unittest import TestCase

from PySearch.Search.RankedSearch import ranked_search


class TestSearch(TestCase):

    def test_ranked_search(self):
        self.assertEqual(ranked_search("kaffe"), ["/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil1.txt"])

    def test_search_mult_word(self):
        self.assertEqual(ranked_search("dette kaffe"), ['/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil3.txt', "/Users/Hans/Documents/Kode/sommerprosjekt17/testfiler/fil1.txt" ])
        # self.assertEqual(search("kaffe sommer"), [])


if __name__ == "__main__":
    unittest.main()