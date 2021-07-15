#!/usr/bin/python3

"""
PE005: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""

import functools
from .utils import lcm

def main(n=20):
    """ Return the smallest integer evenly divisible by all 1 <= k <= n. """
    return functools.reduce(lcm, range(1, 20))
