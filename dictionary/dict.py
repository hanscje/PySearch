


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
        posting = self.data[docID]
        if posting is None:
            self.data[docID] = (1,[position])
            print(self.data[docID])
        else:
            print(self.data[docID])
            self.data[docID] = (posting[0]+1, posting[1].append(position))
            print(self.data[docID])


class Dictionary(object):

    def __init__(self):
        self.data = {}

    def add_word(self, word, docID, position):
        poslist = self.data[word]
        if poslist is None:
            self.data[word] = PostingList()
        self.data[word].add_posting(docID, position)


