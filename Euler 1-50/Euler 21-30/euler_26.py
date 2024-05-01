"""
Reciprocal Cycles
--------------------
A unit fraction contains 1 in the numerator. The following are decimal representations 
of the unit fractions with denominators 2-7:
1/2 = 0.5, 1/3 = 0.(3), 1/4 = 0.25, 1/5 = 0.2, 1/6 = 0.1(6), 1/7 = 0.(142857)
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
Find the value d < n for which 1/d contains the longest recurring cycle in its 
decimal fraction part.
"""

import math

def carmichael(n):
    """ give the smallest positive integer that, when raised to the power of any integer coprime to n, 
    yields 1 modulo n. """
    result = 1
    """ if n is even, left shift by 1 and divide it by 2 until it's odd. """
    if not n & 1:
        result <<= 1
        while not n & 1:
            n >>= 1
          
    p = 3
    sqrt_n = math.isqrt(n)
    """  iterate through odd numbers from 3 to sqrt(n), as if p is a prime divisor of 
    n, p ≤ n. """
    while p <= sqrt_n:
        """ if p divides n, update result by finding the LCM of the result and p - 1, 
        where p - 1 is the order of p mod n (i.e. the smallest positive integer k 
        such that p^k ≡ 1 mod n)."""
        if n % p == 0:
            result = _lowest_common_multiple(result, p - 1) # see Python-Project-Euler/Euler 1-50/Euler 1-10/euler_5.py
            while n % p == 0:
                """ divide n by p whilst it's still divisible, removing all 
                occurrences of p from n. """
                n //= p
            sqrt_n = math.isqrt(n)
        p += 2
        
    """ n itself is prime, so update result by finding the LCM of the result and n 
    − 1, as the order of n mod n is n − 1. """
    if n > 1:
        result = _lowest_common_multiple(result, n - 1)
    return result

def longest_reciprocal_cycle(nums, base=10):
    """ the recurring part for 1/d is the same length as 1/(2d), so it has 
    already been found when analyzing the length of 1/(2d). """
    lower_bound = nums >> 1
    max_order = 0
    max_integer = 0
    max_order_found = False
    i = nums

    while i > lower_bound and not max_order_found:
        d = i
        """ 1 / ((2^a) * (5^b) * d) is the same length as 1/d. Furthermore, if d is 
        coprime to 10, 1/d is purely recurring, so remove all powers of 2 and 5. """
        while d % 2 == 0:
            d >>= 1
        while d % 5 == 0:
            d //= 5

        """ 1/d is nonrecurring if d is of the form (2^a) * (5^b). """
        if d != 1:
            """ the length of the repeating decimal is the multiplicative order of 
            10 mod d. """
            limit = carmichael(d)
            remainder = 1
            order = 1
            found_cycle = False

            while (order << 1) <= limit and not found_cycle:
                remainder = (base * remainder) % d
                if remainder == 1:
                    found_cycle = True
                else:
                    order += 1

            if remainder != 1:
                order = limit

            """ a number x < order + 1 such that 1/x will have > order repeating digits 
            will never be encountered. """
            if lower_bound < order:
                lower_bound = order
            if max_order < order:
                max_order = order
                max_integer = i

            """  order can be no greater than i - 1, and there is no d > i, 
            such that 1/d has > i - 1 repeating digits. """
            if order == i - 1:
                max_order_found = True
        i -= 1
    return max_integer

if __name__ == "__main__":
    print(longest_reciprocal_cycle(1000))
