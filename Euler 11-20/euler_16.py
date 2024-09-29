""" Power Digit Sum
-------------------------------
Sum the digits of n^exp."""

import math

def power_digit_sum(n, exp):
    """ number of digits in the result. """
    order = 0
    """ math.floor() rounds a number down to the nearest integer. math.log10() returns 
    the base-10 logarithm of a number (i.e. the exponent to which 10 must be raised to 
    produce n). This forms the lemma for the length of a number L(n). """
    number = [0] * math.floor((1 + exp * math.log10(n)))
    number[0] = 1
  
    for _ in range(exp):
        carry = 0
        for j in range(order + 1):
            """ calculate the product of the current digit of n and corresponding digit
            of result, plus any carry from the previous iteration. """
            product = n * number[j] + carry
            """ update the current digit of the result with the units place of the 
            product. """
            number[j] = product % 10
            """ update carry with the tens place of the product. """
            carry = product // 10
  
        """ until there's no carry left.  """
        while carry > 0:
            order += 1
            """ update the next digit of the result with the units place of the carry. """
            number[order] = carry % 10
            """ update carry with the tens place of the carry, after incrementing order 
            to accommodate the new digit. """
            carry //= 10
    return sum(number)

if __name__ == "__main__":
  print(power_digit_sum(2, 1000))
