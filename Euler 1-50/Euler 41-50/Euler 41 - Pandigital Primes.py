""" calculates the largest 'n'-digit pandigital prime. """
from itertools import permutations

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def largestPandigitalPrime():
    digits = "7654321"
    """ '.permutations()' takes an iterator and ‘r’ (length of permutation needed) and assumes ‘r’ as the default length of iterator if not mentioned, and returns all possible permutations of length ‘r’ each. """
    for n in range(7, 0, -1):
        """ for each 'n', generate all possible permutations of the first 'n' digits in 'digits'. """
        for perm in permutations(digits[:n]):
            num = int("".join(perm))
            """ if 'num' is prime, it return it as the largest PP; otherwise, continue to the next permutation. """
            if isPrime(num):
                return num
    return None

print(largestPandigitalPrime())
