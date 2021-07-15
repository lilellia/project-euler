#!/usr/bin/python3

"""
PE014: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above one million.
"""

import itertools
from .utils import primes


def collatz(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def main(n=1_000_000):
    """ Return the longest Collatz chain whose starting term < n """
    lengths = {1: 1}

    for k in range(2, n):
        if k in lengths:
            # we've already done this one
            continue

        chain = [k]
        while k not in lengths:
            # go until we see something we've already cached
            k = collatz(k)
            chain.append(k)            

        # add lengths for everything in this chain    
        for i, elem in enumerate(reversed(chain), start=lengths[k]):
            lengths[elem] = i
    
    # sort the results (values < n) by decreasing chain length
    result = sorted(((k, v) for k, v in lengths.items() if k < n), key=lambda item: item[1], reverse=True)
    return result[0][0]