# -*- coding: utf-8 -*-



from PySearch.FileFinder.PathFinder import find_all_files
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

    for line in file:
        for word in line.split():
            invertedindex.add_word(word, 1, 1)

    invertedindex.print_index()


if __name__ == "__main__" :
    index_files()
