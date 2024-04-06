"""
10001st Prime
------------------
By listing the first six primes (2, 3, 5, 7, 11, and 13), 13 is the 6th.
Find the nth prime.
"""

import math
import numpy as np

def nth_prime(n):
    """ prime number theorem: the nth prime is ~ n * ln(n), 
    where ln is the natural logarithm. """
    limit = 2 * (n * int(math.log(n)))
    primes = np.ones(limit, dtype=bool)
    """ mark evens (except two), and multiples of 3 (excluding 3), as composite. """
    primes[:2] = primes[4::2] = primes[9::6] = False

    prime_count = 1
    """ candidate to be tested for primality. """
    p = 3
    """ keep testing until n primes have been found. """
    while prime_count < n:
        if primes[p]:
            prime_count += 1
            if prime_count == n:
                return p
            """ mark multiples of 3 as composite. """
            primes[p * p:: 2 * p] = False
        """ skip evens. """
        p += 2
      
if __name__ == "__main__":
    print(nth_prime(10001))
