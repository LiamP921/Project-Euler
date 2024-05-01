"""
Factorial Digit Sum
-----------------------
The digit sum of 10! (10 × 9 × ... × 3 × 2 × 1 = 3628800) is 3 + 6 + 2 + 8 + 8 + 0 + 0 
= 27.
Find the sum of the digits n!
"""

import math

def factorial_digit_sum(n):
    """ combine length lemma from #16 with Stirling's asympotic approximation for the 
    length of a factorial. math.floor() rounds a number down to the nearest integer. math.pi 
    returns the constant value of pi, which is used as a scaling factor, as is Euler's 
    number, e, via math.e. """
    digits = math.floor(0.5 * math.log10(2 * math.pi * n) + n * math.log10(n / math.e)) + 1
    result = [0] * digits
    result[0] = 1

    for i in range(2, n + 1):
        carry = 0
        """ for each digit, compute its product with the current value of i and 
        add the carry from the previous calculation. """
        for j in range(digits):
            product = i * result[j] + carry
            """ this gives the digit to be placed at that position, and the 
            quotient gives the carry for the next calculation. """
            result[j] = product % 10
            carry = product // 10

        """ if there is any remaining carry, increase the number of digits in the 
        result and update the last digit accordingly. """
        while carry > 0:
            digits += 1
            result[digits - 1] = carry % 10
            carry //= 10
    return sum(result)
