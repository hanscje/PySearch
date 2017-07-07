from PySearch.FileReader.readFiles import index, docID_to_path
from PySearch.Tokenizer.tokenize import tokenize


def search(query):

    inverted_index = index()
    query_terms = tokenize(query)
    if not query_terms:
        return []
    result_list = []
    docIDs = []

    for term in query_terms:
        docIDs.append(inverted_index.get_posting_list(term).get_keys())


    base_list = docIDs[0]
    for list in docIDs[1:]:
        base_list = merge(base_list, list)

    for id in base_list:
        result_list.append(docID_to_path(id))

    return result_list


def merge(list1, list2):
    set2 = set(list2)
    return [val for val in list1 if val in set2]

if __name__ == "__main__" :
    print(search("kaffe"))
    print(search("dette"))
