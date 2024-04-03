"""
Largest Prime Factor
-----------------------
The prime factors of 13195 are 5, 7, 13 and 29.
Find the largest prime factor of n.
"""

import math

def largest_prime_factor(n):
    i = 2
    """
     if there is a factor of n > sqrt(n), the other would be necessarily < sqrt(n),
     and would have already been encountered.
    """
    while i <= math.sqrt(n):
        """
        remove the factor i from n
        """
        if n % i == 0:
            n //= i
        else:
            i += 1
    """
    n will be the largest prime factor, as it's continuously divided by its smallest
    prime factors until it becomes prime.
    """
    return n

print(largest_prime_factor(600_851_475_143))
