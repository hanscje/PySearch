# -*- coding: utf-8 -*-

from PySearch.FileFinder.PathFinder import find_all_files
from PySearch.dictionary.dict import Dictionary

invertedindex = Dictionary()

def get_files():
    files = find_all_files("/Users/Hans/Documents/Kode/sommerprosjekt17")
    files = filter(lambda x : x.endswith(".txt") or x.endswith(".py"), files)
    print(files)
    for file in files:
        index_file(file)

def index_file(filename):
    print(filename)
    file = open(filename, "r", encoding='utf-8')

    for line in file:
        for word in line.split():
            invertedindex.add_word(word, 1, 1)



if __name__ == "__main__" :
    get_files()