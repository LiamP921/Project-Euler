"""
Power Digit Sum
-----------------
Sum the digits of n^exp.
"""

import math

def power_digit_sum(n, exp):
    """ math.log10() returns the base-10 logarithm of a number (i.e. 
    the exponent to which 10 must be raised to produce n).
    This forms the lemma for the length of a number L(n). """
    length = int(exp * (math.log10(n))) + 1
    """ Shift the decimal i places right to effectively isolate the digit at position i. 
    Then, extract the last digit via % 10 and sum it. """
    return sum(int(n ** exp // 10 ** i % 10) for i in range(length))

if __name__ == "__main__":  
    print(power_digit_sum(2, 1000))
