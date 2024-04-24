"""
Goldbach's Other Conjecture
-----------------------------
Goldbach incorrectly proposed that every odd composite number can be written 
as the sum of a prime and twice a square. 9 = 7 + 2 * 12, 15 = 7 + 2 * 22, 21 
= 3 + 2 * 32, 25 = 7 + 2 * 32, 27 = 19 + 2 * 22, 33 = 31 + 2 * 12.

Calculate the smallest odd composite that can't be written as the sum of a 
prime and twice a square.
"""

import math

def goldbachs_other_conjecture():
    n = 33
    primes = set()

    while True:
        """ n is prime if it's divisible by all primes in the set. """
        if all(n % p for p in primes):
            primes.add(n)
        else:
            """ if a non-prime n can be expressed as the sum of a prime and twice a 
            square. """
            if not any((n - 2 * i * i) in primes for i in range(2, math.isqrt(n // 2) + 1)):
                return n
        n += 2

if __name__ == "__main__":
    print(goldbachs_other_conjecture())
