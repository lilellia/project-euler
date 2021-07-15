#!/usr/bin/python3

"""
PE001: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from .utils import lcm, triangle


def main(a=3, b=5, n=1000):
    """ Return the sum of all integers 1 <= k < n such that a divides k or b divides k. """
    # Observe that the desired sum is S = (a + 2a + 3a + ... + Aa) + (b + 2b + 3b + ... + Bb) where A, B are the largest integers such that Aa < n and Bb < n.
    # However, this double-counts all multiples of the lcm(a, b) since these values appear in both fragments of that sum. Thus, write
    # S = a(1 + 2 + ... + A) + b(1 + 2 + ... + B) - m(1 + 2 + ... + M), where m=LCM(a, b) and M is the largest integer with Mm < n.
    #   = a*triangle(A) + b*triangle(B) - m*triangle(M), where triangle(k) = k(k+1)/2.

    m = lcm(a, b)
    A, B, M = [(n - 1) // val for val in (a, b, m)]

    return a * triangle(A) + b * triangle(B) - m * triangle(M)


if __name__ == '__main__':
    print(main(a=3, b=5, n=10))