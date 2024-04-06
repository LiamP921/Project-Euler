"""
Special Pythagorean triplet
-----------------------------
Pythagorean triplets are sets of three naturals, a < b < c, for which, a^2 + b^2 = c^2
(e.g. 32 + 42 = 9 + 16 = 25 = 52).
Find the product(s) abc such that a + b + c = sum_value.
"""

import math

def special_pythagorean_triplets(sum_value):
    """ ensures that ensures m doesn't exceed half of isqrt(sum_value)
    since a + b + c = sum_value, and a < b < c, a will be less than half 
    of sum_value. """
    upper_bound = math.isqrt(sum_value // 2) + 1

    for m in range(2, upper_bound):
        """ ensure that the sum_value can be divided into two integers. """
        if (sum_value // 2) % m == 0:
            """ iterate through all possible k values to find a suitable m and n value;
            range ensures that k > m and k is even. """
            k_start = m + 1 if m % 2 == 0 else m + 2

            for k in range(k_start, 2 * m, 2):
                """ Euclid's Formula: any Pythagorean triplet can be represented as: 
                a = m^2 - n^2, b = 2mn, c = m^2 + n^2, where m > n. These are both
                coprime positive integers (i.e have no common factors other than 1). """
                if (sum_value // (2 * m)) % k == 0 and _greatest_common_divisor(k, m) == 1: # see Euler 1-50/Euler 1-10/euler_5.py
                    divisor = sum_value // 2 // (k * m)
                    n = k - m
                    a = divisor * (m ** 2 - n ** 2)
                    b = 2 * divisor * m * n
                    c = divisor * (m ** 2 + n ** 2)
                    yield a * b * c
                  
if __name__ == "__main__":
  for product in special_pythagorean_triplets(1000):
    print(product)
