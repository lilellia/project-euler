#!/usr/bin/python3

"""
PE010: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

import itertools
from .utils import primes


def main(n=2_000_000):
    """ Return the sum of primes < n. """
    return sum(itertools.takewhile(n.__gt__, primes()))
