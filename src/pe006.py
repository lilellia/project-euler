#!/usr/bin/python3

"""
PE006: Sum square difference

The sum of the squares of the first ten natural numbers is,
    1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is
    3025 - 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

from .utils import triangle, square_pyramid

def main(n=100):
    """ Return (1 + 2 + ... + n)² - (1² + 2² + ... + n²) """
    return triangle(n) ** 2 - square_pyramid(n)
    
