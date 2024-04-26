"""
Prime Permutations
---------------------
1487, 4817, 8147 is unusual: each of the three terms is prime, whilst being 4-digit 
permutations of one another. There are no arithmetic sequences made up of three 
1-, 2-, or 3-digit primes, exhibiting this property, but there is another 4-digit one.

Find the 12-digit integer formed by concatenating the three terms in this sequence.
"""

import itertools

def _get_permutations(n):
    """ keys are the sorted digits of the primes, values are lists of primes 
    with the same digits. """
    permute_primes = {}
    for p in _eratosthenes(n): # see Python-Recreational-Mathematics/primality/sieves/eratosthenes.py
        """ .setdefault() returns the value of a key. """
        permute_primes.setdefault("".join(sorted(str(p))), []).append(p)
    """ .values() returns a view object listing all the values in a dictionary. """
    for perms in permute_primes.values():
        """ itertools.combinations() returns r length subsequences of 
        elements from the input iterable in lexicographic order. """
        for a, b, c in itertools.combinations(perms, 3):
            assert c > b > a
            yield a, b, c

def prime_permutations():
    permutations = _get_permutations(10000)
    for x, y, z in permutations:
        """ abs() returns the absolute value (non-negative value regardless 
        of sign) of a number. """
        if abs(x - y) == abs(y - z) and x != 1487:
            """ if the difference between consecutive terms is the same. """
            return "".join([str(x), str(y), str(z)])

if __name__ == '__main__':
    print(prime_permutations())
