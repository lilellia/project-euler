import collections
import itertools
import math


def triangle(k: int) -> int:
    """ Return the kth triangle number. """ 
    return k * (k + 1) // 2


def lcm(a, b):
    """ Return the least common multiple of a and b. """
    return a * b // math.gcd(a, b)


def fibonacci(a=0, b=1):
    yield a
    while True:
        yield b
        a, b = b, a+b


def primes():
    """ Iterate over the primes.
    https://stackoverflow.com/a/568618
    """
    witnesses = {}

    for q in itertools.count(2):
        # q is the running integer being tested
        if q not in witnesses:
            # q is a new prime.
            # yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield q
            witnesses[q * q] = [q]
        else:
            # q is composite. witnesses[q] is the list of primes
            # that divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next multiples
            # of its witnesses to prepare for larger numbers
            for p in witnesses[q]:
                witnesses.setdefault(p + q, []).append(p)
            del witnesses[q]


def prime_factorization(n: int):
    """ Return a dictionary of the form {p: a}, indicating that p**a divides n. """
    result = collections.defaultdict(int)
    for p in primes():
        if n == 1:
            return result
        
        count = 0
        while n % p == 0:
            result[p] += 1
            n //= p