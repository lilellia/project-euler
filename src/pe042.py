#!/usr/bin/python3

"""
PE042: Coded triangle numbers


The nth term of the sequence of triangle numbers is given by,
T(n) = n(n+1)/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to
its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = T(10).
If the word value is a triangle number then we shall call the word
a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand
common English words, how many are triangle words?
"""

import math
import pathlib
import re
import string
from .utils import triangle


def is_triangle(t: int):
    # if t is a triangle number, then t = n(n+1)/2 for some integer n
    # => 2t = n^2 + n
    # => n^2 + n - 2t = 0
    # => n = (-1 +/- sqrt(1 + 8t)) / 2
    # => 1 + 8t is a perfect square
    s = math.sqrt(1 + 8 * t)
    if s.is_integer():
        n = (-1 + s) / 2
        if n.is_integer() and triangle(n) == t:
            return True
    return False



PATH_TO_FILE = pathlib.Path(__file__).parent.parent / 'lib' / 'p042_words.txt'
def main(fp=PATH_TO_FILE):
    """ Return the number of triangle words in the file """
    with open(fp) as f:
        words = re.findall(r'"([A-Z]+)"', f.read())

    return sum(
        is_triangle(sum(1+string.ascii_uppercase.index(c) for c in word))
        for word in words
    )