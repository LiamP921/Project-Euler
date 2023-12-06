""" calculates the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the 
same digit, is part of an 'n' prime value family. """
import numpy as np
from math import isqrt
from itertools import combinations

def sieveOfEratosthenes(limit):
  if limit < 2:
      return 
  size = (limit - 1) // 2
  """ 'np.ones()' returns a new array of the given shape and data type, with values of '1'; acts as a primality tracker. """
  prime = np.ones(size + 1, dtype=bool)

  """ '.isqrt()' gets the integer square root of the given non-negative integer 'n'. It returns the floor value of the exact sqrt 
  of 'n', or equivalently the greatest integer 'a' such that 'a^2 <= n'. """
  for i in range(1, isqrt(limit) // 2 + 1):
      if prime[i]:
          p = i * 2 + 1
          """ updates all elements of 'prime' that correspond to multiples of the current prime 'p'. """
          prime[i + p::p] = False
  """ '.concatenate()' joins two or more arrays along a specified axis; '.nonzero()' computes the indices of non-zero elements, 
  returning a tuple of arrays, one for each dimension, containing said indices that dimension."""
  primes = np.concatenate(([2], np.nonzero(prime)[0] * 2 + 1))
  return primes

def replaceDigits(n, digits, replacement):
    n_str = str(n)
    """ iterate over the stringified digits to be replaced. """
    for digit in digits:
        """ replace the digit with the given replacement. """
        n_str = n_str[:digit] + replacement + n_str[digit + 1:]
    return int(n_str)

def findSmallestPrimeFamily(family_size, n, primes):
    prime_set = set(primes)
    """ '.reversed()' reverses a given sequence object and returns it as a list."""
    for prime in reversed(primes):
        prime_str = str(prime)
        """ counts the number the occurrences of each digit in the prime. """
        digit_count = {}
        """ iterates over the digits of the prime and stores their positions in 'digit_count'. """
        for i in range(len(prime_str)):
            if prime_str[i] in digit_count:
                digit_count[prime_str[i]].append(i)
            else:
                digit_count[prime_str[i]] = [i]

        """ iterates over the digits and their positions in 'digit_count'; '.items()' 
        returns a view object that displays a list of dictionary's (key, value) tuple pairs. """
        for digit, indices in digit_count.items():
            """ if there are at least two instances of the digit in the prime """
            if len(indices) >= 2:
                """ generates combinations of indices of the digit to be replaced; 'combinations(iterable, r)' returns the 
                length subsequences of elements from the input iterable. """
                for combo_length in range(1, len(indices) + 1):
                    for combo in combinations(indices, combo_length):
                        """ counts the number of prime replacements and tracks the smallest prime in the family. """
                        count = 0
                        smallest_prime = prime
                        for replacement in '0123456789':
                            """ skip the replacement if it would result in a number with '0' as its leading digit; 'continued skips the remaining statements
                            in the current loop and starts the next iteration. """
                            if replacement == '0' and combo[0] == 0:
                                continue
                            """ replace the selected digit combination and check if the resulting number is in 'prime_set'. """
                            new_prime = replaceDigits(prime, combo, replacement)
                            if new_prime in prime_set:
                                count += 1
                                if new_prime < smallest_prime:
                                    smallest_prime = new_prime
                        """ if the count reaches the specified family size, return the smallest prime in the family. """
                        if count == family_size:
                            return smallest_prime

if __name__ == '__main__':
    limit = 1000000
    primes = sieveOfEratosthenes(limit)
    result = findSmallestPrimeFamily(8, limit, primes)
    print(result)
