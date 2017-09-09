
"""
    datastruktur:

        self.data er ordboken
        data inneholder postingliste, postingliste er en klasse som inneholder en Dictionary av postings som kan være
        klasse eller tupler.

        self.data = Dictionary { word : postinglist { docID : Posting (antall, posision[]) } }


"""


# TODO: lag noe som mapper mellom DocID og Path


class PostingList(object):

    def __init__(self):
        self.data = {}

    def add_posting(self, docID, position):
        posting = self.data.get(docID, None)
        if posting is None:
            positions = [position]
            self.data[docID] = (1, positions)
        else:
            modified_count = posting[0]+1
            modified_positions = posting[1]
            modified_positions.append(position)
            self.data[docID] = (modified_count, modified_positions)

        return self

    def print_postings(self):
        for docID, posting in self.data.items():
            print("\tdocID:", docID, ":\t#postings", posting[0])

    def get_keys(self):
        key_list = list(self.data.keys())
        return key_list

    def get_count(self, docID):
        return self.data.get(docID)[0]

    def get_position_list(self, docID):
        return self.data.get(docID)[1]

    def get_size(self):
        return len(self.data)

    def get_postings(self):
        return self.data


class Dictionary(object):

    def __init__(self):
        self.data = {}
        self.corpus_size = 0

    def add_word(self, word, docID, position):
        if docID > self.corpus_size: self.corpus_size = docID
        posting_list = self.data.get(word, None)
        if posting_list is None:
            self.data[word] = PostingList()

        self.data[word].add_posting(docID, position)

    def get_posting_list(self, word):
        posting_list = self.data.get(word, None)
        if posting_list is None:
            return PostingList()
        else:
            return posting_list

    def print_index(self):
        for key, posting_list in self.data.items():
            print("'"+key+"'")
            posting_list.print_postings()

    def check_word(self, word):
        """
        checks words existence in the dictionary
        :param word: Word to be given realitycheck
        :return: True/False
        """
        if word in self.data:
            return True
        else:
            return False

    def get_corpus_size(self):
        return self.corpus_size + 1
