# -*- coding: utf-8 -*-



from PySearch.FileFinder.PathFinder import find_all_files
from PySearch.Tokenizer.tokenize import tokenize
from PySearch.dictionary.dict import Dictionary

invertedindex = Dictionary()

def index_files():
    """
    Made to keep get_files and index_file clean

    :return: void
    """
    files = get_files()
    for file in files:
        index_file(file)



def get_files(root_folder = "/Users/Hans/Documents/Kode/sommerprosjekt17"):
    """
    Gets all the file names from a specified folder, in string format.
    Filters the files on a filter. To avoid hidden and unwanted files.

    Here it calls for files from pathFinder module.

    :param root_folder: the rootfolder for which all files and subdirs is returned
    """
    files = find_all_files(root_folder)

    #Filters files so we dont get hidden files
    files = filter(lambda x : x.endswith(".txt") or x.endswith(".py"), files)

    return files

def index_file(filename):
    """

    :param filename:
    :return:
    """


    file = open(filename, "r", encoding='utf-8')

    word_counter = 0
    for line in file:
        words_in_line = tokenize(line)
        for word in words_in_line:
            invertedindex.add_word(word, 1, word_counter)
            word_counter += 1




if __name__ == "__main__" :
    index_files()
    invertedindex.print_index()
