"""
Amicable Numbers
------------------
d(n) is the sum of n's proper divisors (numbers < n which divide evenly into it).
If d(a) = b and d(b) = a, where a ≠ b, a and b are an amicable pair, and are each 
called amicable numbers.
Sum all amicable numbers < n.
"""

import math

def _proper_divisors(n):
    if n in memo:
      return memo[n]
  
    sieve = [1] * (n + 1)
    """ account for when i is a proper divisor of i * i. """
    for i in range(2, math.isqrt(n) + 1):
        sieve[i * i] += i
        """ iterate over multiples of i. """
        for j in range(i * (i + 1), n + 1, i):
            sieve[j] += i + j // i
  
    memo[n] = sieve
    return sieve

def amicable_numbers(limit):
    amicable_sum = 0
    sieve = _proper_divisors(limit)
    """ if the sum of k's proper divisors (sieve[k]) < k and if the sum of proper divisors 
      of sieve[k] == k, k and sieve[k] form an amicable pair. """
    for k in range(limit):
        if sieve[k] < k and sieve[sieve[k]] == k:
            amicable_sum += k + sieve[k]
    return amicable_sum

if __name__ == "__main__":
    memo = {}
    print(amicable_numbers(10000))
