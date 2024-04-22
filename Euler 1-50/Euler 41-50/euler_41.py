"""
Pandigital Prime
-------------------
An n-digit number is pandigital if it uses all the digits 1 to n exactly once. 
Find the largest n-digit pandigital prime.
"""

import itertools

def pandigital_prime(n):
    """ pandigital primes can only be 4 or 7 digits, as every other 
    pandigital number's digit sum is divisible by 3. """
    if n not in [4, 7]:
        return None
    """ map() returns a list of results after applying the given function to each 
    item of a given iterable """
    digits = set(map(str, range(1, n + 1)))
    largest_pandigital_prime = 0
    """ itertools.permutations() returns length permutations of elements in an 
    iterable (either a specified number of times or until the iterable is exhausted) 
    in lexicographic order. """
    for i in itertools.permutations(digits, n):
        permutation_number = int("".join(i))
        if _miller_rabin(permutation_number): # see Python-Recreational-Mathematics/primality/miller_rabin.py
            largest_pandigital_prime = max(largest_pandigital_prime, permutation_number)
    return largest_pandigital_prime

if __name__ == "__main__":
  print(pandigital_prime(7))
