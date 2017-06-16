

from PySearch.FileFinder.PathFinder import find_all_files


def get_files():
    files = find_all_files("/Users/Hans/Documents/Kode/sommerprosjekt17")
    for file in files:
        index_file(file)

def index_file(filename):
    print(filename)

if __name__ == "__main__" :
    get_files()