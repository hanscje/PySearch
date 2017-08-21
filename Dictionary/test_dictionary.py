from unittest import TestCase

from PySearch.Dictionary.dict import Dictionary


class TestDictionary(TestCase):

    def setUp(self):
        self.dict = Dictionary()
        self.dict.add_word("hei",1,2)

    def test_get_posting_list(self):
        pst_lst = self.dict.get_posting_list("hei")
        self.assertIsNotNone(pst_lst)

    def test_check_word(self):
        self.assertTrue(self.dict.check_word('hei'))
        self.assertFalse(self.dict.check_word('jeg'))

    def test_add_word(self):
        self.dict.add_word('test', 2,4)
        self.assertTrue(self.dict.check_word('test'))

    def test_get_corpus_size(self):
        self.assertEqual(self.dict.get_corpus_size(), 2)

    def tearDown(self):
        self.dict = None


if __name__ == "__main__":
    unittest.main()