#!/usr/bin/python3

"""
PE009: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which a² + b² = c².

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def main():
    """ Return the product abc for Pythagorean triplet (a, b, c) with a+b+c = 1000 """
    # Since a < b < c, we have a + b + c = 1000 > a + a + a, making a < 334.
    for a in range(1, 334):
        # Then b + c = 1000 - a > b + b, making b < 500 - a/2.
        for b in range(a + 1, 501 - a // 2):
            c = 1000 - a - b

            # check for Pythagorean triplet
            if a * a + b * b == c * c:
                return a * b * c