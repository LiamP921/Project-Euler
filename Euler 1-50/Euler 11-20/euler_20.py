"""
Factorial Digit Sum
-----------------------
The digit sum of 10! (10 × 9 × ... × 3 × 2 × 1 = 3628800) is 3 + 6 + 2 + 8 + 8 + 0 + 0 
= 27.
Find the sum of the digits n!
"""

import math

def sum_digits_factorial(n):
    """ combine length lemma from problem #16 with Stirling's asympotic approximation 
    for the length of a factorial. math.floor() rounds a number down to the nearest integer. 
    math.pi returns the constant value of pi, which is used as a scaling factor, as is Euler's 
    number,e, via math.e. """
    length = 1 + math.floor(0.5 * math.log10(2 * math.pi * n) + n * math.log10(n / math.e))
    fac = _factorial(n) # see Python-Project-Euler/Euler 1-50/Euler 11-20/euler_15.py
    return sum(int(fac // 10 ** i % 10) for i in range(length))

if __name__ == "__main__":
  print(sum_digits_factorial(100))
