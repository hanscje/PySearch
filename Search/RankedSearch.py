import math

from PySearch.FileReader.readFiles import index, docID_to_path
from PySearch.Tokenizer.tokenize import tokenize


def rank_documents(query_terms):
    inverted_index = index()
    result_set = {}
    total_number_of_docs = inverted_index.get_corpus_size()

    for term in query_terms:
        posting_list = inverted_index.get_posting_list(term)

        if posting_list is None:
            print("Hei, det er ingen posting-liste")
            continue

        idf = math.log(total_number_of_docs/posting_list.get_size(), 10)
        print("idf verdien", idf)
        postings = posting_list.get_postings()
        print(postings)
        if postings is None:
            print("Hei! postings er tom!")

        for docID, posting in postings.items():

            if docID in result_set:
                result_set[docID] = result_set[docID] + posting[0]*idf # posting[0] er tf
            else:
                result_set[docID] = float(posting[0])*idf

    return result_set


def ranked_search(query):
    query_terms = tokenize(query)
    print(query_terms)
    results = rank_documents(query_terms)
    sorted_results = [(doc, results[doc]) for doc in sorted(results, key=results.get, reverse=True)]

    for d, rank in sorted_results:
        path = docID_to_path(d)
        print("Hei!")
        print(path, rank)

if __name__ == '__main__':
    #print("Hei!")
    ranked_search("kaffe")