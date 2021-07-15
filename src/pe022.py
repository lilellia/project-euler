#!/usr/bin/python3

"""
PE022: Names scores

Using names.txt, a 46K text file containing over five-thousand first
names, begin by sorting it into alphabetical order. Then working out
the alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import pathlib
import re
import string


PATH_TO_FILE = pathlib.Path(__file__).parent.parent / 'lib' / 'p022_names.txt'

def main(fp=PATH_TO_FILE):
    """ Return the total score for names in the file """
    with open(fp) as f:
        names = sorted(re.findall(r'"([A-Z]+)"', f.read()))

    return sum(
        i * sum(1 + string.ascii_uppercase.index(c) for c in name)
        for i, name in enumerate(names, start=1)
    )
