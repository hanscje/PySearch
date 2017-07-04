"""
Tokenize words.

@author hjenvild@gmail.com, arildlil@protonmail.com
"""


def tokenize(line):

    # split_chars = ["\\", "'", ")"]


    assert isinstance(line, str), "The input is not a string, was a %r"%type(line)

    ord = line.strip().split()
    return ord

