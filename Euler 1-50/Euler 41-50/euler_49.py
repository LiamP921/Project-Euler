"""
Prime Permutations
---------------------
The sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual: each of the three terms are primes that are 4-digit permutations of one another. 
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is another 4-digit one.

Find the 12-digit integer formed by concatenating the three terms in this sequence.
"""

def _is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))

def prime_permutations():
    n, f = 1487, 1 
    while True:
        n += 3 - f
        f = -f
        b, c = n + 3330, n + 6660
        if all(_miller_rabin(num) for num in (n, b, c)) and _is_perm(n, b) and _is_perm(b, c): # see Python-Recreational-Mathematics/primality/sieves/miller_rabins.py
            return "".join([str(n), str(b), str(c)])

if __name__ == "__main__":
    print(prime_permutations())
