"""
Given a start directory finds all file names in current dir, and recursively
"""
import os

initpath = os.getcwd()
startpath = initpath


#def filewalk():


def init(path = os.getcwd()):
    """
    initializes a wanted indexing directory

    :param path: wanted startpath
    :return: nothing you greede b*
    TODO: sjekk at path ikke er en fil, men mappe
    """

    startpath = path
    os.chdir(startpath)


def findAllFiles():
    """
    Find all files in subdirectory of "startpath"

    :return:list of all files in subdir
    """

    files = os.walk(startpath)
    filepaths = []
    for tuple in files:
        for filename in tuple[2]:
            fullpathname = os.path.join(tuple[0],filename)
            filepaths.append(fullpathname)

    return filepaths




if __name__ == "__main__":
    print("Tut, Tut")
    init("/Users/Hans/Documents/Kode/sommerprosjekt17/PySearch")


