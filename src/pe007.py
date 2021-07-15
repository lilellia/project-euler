#!/usr/bin/python3

"""
PE007: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import itertools
from .utils import primes


def main(n=10001):
    """ Return the nth prime. """
    return next(itertools.islice(primes(), n - 1, None))
