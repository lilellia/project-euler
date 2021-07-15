#!/usr/bin/python3

"""
PE004: Largest palindrome product


A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from .utils import prime_factorization


def main(n=3):
    """ Return the largest palindrome product of n-digit numbers. """
    bound = pow(10, n) - 1

    maximum = None
    for a in range(bound, 0, -1):
        if maximum and a * bound < maximum:
            # everything from here on is smaller than what we've found
            return maximum

        for b in range(bound, 0, -1):
            if maximum and a * b < maximum:
                # we can't get any value from here that's > maximum
                break

            product = a * b
            if str(product) == str(product)[::-1]:
                maximum = product
