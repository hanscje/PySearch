import unittest
from unittest import TestCase

from PySearch.Dictionary.dict import PostingList


class TestPostingList(TestCase):

    def setUp(self):
        self.postinglst = PostingList()
        self.postinglst.add_posting(1, 3)
        self.postinglst.add_posting(1, 5)
        self.postinglst.add_posting(1, 6)
        self.postinglst.add_posting(3, 3)
        self.postinglst.add_posting(5, 6)

    def test_get_keys(self):
        self.assertEqual(self.postinglst.get_keys(), [1,3,5])

    def test_add_keys(self):
        self.assertEqual(self.postinglst.add_posting(7, 4).add_posting(2, 5).get_keys(), [1, 2, 3, 5, 7])
        self.assertEqual(self.postinglst.add_posting(7, 4).add_posting(7, 5).get_keys(), [1, 2, 3, 5, 7])

    def test_get_count(self):
        self.assertEqual(self.postinglst.get_count(1), 3)

    def test_get_pos_lst(self):
        self.assertEqual(self.postinglst.get_pos_lst(1), [3,5,6])

    def tearDown(self):
        self.postinglst = None


if __name__ == "__main__":
    unittest.main()