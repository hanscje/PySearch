"""
Tokenize words.

__author__ = hjenvild@gmail.com, arildlil@protonmail.com
"""
import re


def tokenize(line):

    assert isinstance(line, str), "The input is not a string, was a %r"%type(line)

    line = line.strip().lower()
    ord = re.split("([^a-zA-Z0-9æøåÆØÅ])", line)
    ord = [o for o in ord if o != ' ' and o != '']
    return ord

