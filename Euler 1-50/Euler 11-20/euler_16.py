"""
Power Digit Sum
-----------------
Sum the digits of n^exp.
"""

import math

def power_digit_sum(n, exp):
    result = n ** exp
    digit_sum = 0
    """ math.log10() returns the base-10 logarithm of a number (i.e. 
    the exponent to which 10 must be raised to produce n).
    This forms the lemma for the length of a number L(n). """
    for _ in range(1 + int(exp * (math.log10(n)))):
        digit_sum += result % 10
        result //= 10
  
    return digit_sum

if __name__ == "__main__":  
    print(power_digit_sum(2, 1000))
