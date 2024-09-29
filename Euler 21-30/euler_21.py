""" Amicable Numbers
-------------------------
d(n) is the sum of n's proper divisors (numbers < n which divide evenly into it).
If d(a) = b and d(b) = a, where a ≠ b, a and b are an amicable pair, and are each 
called amicable numbers.
Sum all amicable numbers < n. """

import math

def _proper_divisor_sums(n):
    """ sum of proper divisors for each number 1-n. """
    div_sum = [1] * (n + 1) 
    for i in range(2, math.isqrt(n) + 1):
        """ i is a proper divisor of i * i. """
        div_sum[i * i] += i
        """ calculate proper divisors of all multiples of i * i. """
        for j in range(i * i + i, n, i):
            """ i and j // i represents different proper divisors of j. """
            div_sum[j] += i + j // i
    return div_sum

def amicable_numbers(limit):
    amicable_sum = 0
    candidates = _proper_divisor_sums(limit)
    """ if the sum of k's proper divisors (candidates[k]) < k and if the sum of proper divisors 
      of candidates[k] == k, k and candidates[k] form an amicable pair. """
    for k in range(limit):
        if candidates[k] < k and candidates[candidates[k]] == k:
            amicable_sum += k + candidates[k]
    return amicable_sum

if __name__ == "__main__":
    print(amicable_numbers(10000))
