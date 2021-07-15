#!/usr/bin/python3

"""
PE003: Largest prime factor


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

from .utils import prime_factorization


def main(n=600_851_475_143):
    """ Return the largest prime factor of n """
    pf = prime_factorization(n)
    return max(pf.keys())