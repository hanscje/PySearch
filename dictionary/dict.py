
"""
    datastruktur:

        self.data er ordboken
        data inneholder postingliste, postingliste er en klasse som inneholder en dictionary av postings som kan være
        klasse eller tupler.

        self.data = dictionary { wordID : postinglist { docID : Posting (antall, posision[]) } }


    TODO: lag noe som mapper mellom DocID og Path
"""


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


    def print_postings(self):
        for docID, posting in self.data.items():
            print("\t", docID, ":\t", posting[0])




class Dictionary(object):

    def __init__(self):
        self.data = {}

    def add_word(self, word, docID, position):
        posting_list = self.data.get(word, None)
        if posting_list is None:
            self.data[word] = PostingList()

        self.data[word].add_posting(docID, position)

    def print_index(self):
        for key, posting_list in self.data.items():
            print(key)
            posting_list.print_postings()






