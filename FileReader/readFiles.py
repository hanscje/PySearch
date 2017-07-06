# -*- coding: utf-8 -*-

from PySearch.FileFinder.PathFinder import find_all_files
from PySearch.Tokenizer.tokenize import tokenize
from PySearch.dictionary.dict import Dictionary

invertedindex = Dictionary()
id_mapping = []

def index_files():
    """
    Made to keep get_files and index_file clean

    :return: void
    """
    paths = get_files()
    docID = 0
    for file_path in paths:
        id_mapping.insert(docID, file_path)
        index_file(file_path, docID)
        docID += 1


def get_files(root_folder = "/Users/Hans/Documents/Kode/sommerprosjekt17"):
    """
    Gets all the file names from a specified folder, in string format.
    Filters the files on a filter. To avoid hidden and unwanted files.

    Here it calls for files from pathFinder module.

    :param root_folder: the rootfolder for which all files and subdirs is returned
    """
    paths = find_all_files(root_folder)

    # Filters files so we don't get hidden files
    paths = filter(lambda x : x.endswith(".txt") or x.endswith(".py"), paths)

    return paths

def docID_to_path(docID):
    return id_mapping[docID]


def index_file(filename, docID):
    """
    :param filename:
    :return:
    """

    file = open(filename, "r", encoding='utf-8')


    word_counter = 0
    for line in file:
        words_in_line = tokenize(line)
        for word in words_in_line:
            invertedindex.add_word(word, docID, word_counter)
            word_counter += 1


if __name__ == "__main__" :
    index_files()
    invertedindex.print_index()
