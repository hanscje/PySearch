"""
Given a start directory finds all file names in current dir, and recursively
"""
import os

initpath = os.getcwd()
startpath = initpath

def find_all_files(path):
    """
    Find all files in subdirectory of "startpath"

    :return:list of all files in subdir
    """

    files = os.walk(path)
    filepaths = []
    for tuple in files:
        for filename in tuple[2]:
            fullpathname = os.path.join(tuple[0],filename)
            filepaths.append(fullpathname)

    return filepaths
