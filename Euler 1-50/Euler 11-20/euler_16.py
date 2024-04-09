"""
Power Digit Sum
-----------------
Sum the digits of n^exp.
"""

import math

def power_digits_sum(n, exp):
    digit_sum = 0
    """ pow returns x^y, and can find the modulus; math.ceil rounds a number up to 
    the nearest integer. math.log10() returns the base-10 logarithm of a number (i.e. 
    the exponent, the number of times to use a given number in a multiplication, 
    to which 10 must be raised to produce n).
    """
    digits = pow(n, exp, 10 ** math.ceil(1 + exp * math.log10(n)))
  
    while digits:
        digit_sum += digits % 10
        digits //= 10
    return digit_sum
  
if __name__ == "__main__":
    print(power_digits_sum(2, 1000))
