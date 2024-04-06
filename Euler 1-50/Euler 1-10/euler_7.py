"""
10001st Prime
------------------
By listing the first six primes (2, 3, 5, 7, 11, and 13), 13 is the 6th.
Find the nth prime.
"""

import math

def nth_prime(n):
    """ prime number theorem: the nth prime is approximately n * ln(n), 
    where ln denotes the natural logarithm. """
    limit = 2 * n * int(math.log(n))
    primes = [True] * limit
    prime_count = 0

    """ candidate to be tested for primality. """
    p = 2
    """ keep testing until n primes have been found. """
    while prime_count < n:
        if primes[p]:
            prime_count += 1
            if prime_count == n:
                return p
            """ mark composites as non-prime. """
            for i in range(p * p, limit, p):
                primes[i] = False
        p += 1

if __name__ == "__main__":
    print(nth_prime(10001))
