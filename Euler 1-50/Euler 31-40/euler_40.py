"""
Champernowne's Constant
-------------------------
An irrational decimal fraction is created by concatenating the positive integers: 
0.123456789101112131415161718192021... Here, the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, calculate d1 * d10 * 
d10^2, ..., * d10^n
"""

import functools
import operator

def _find_digit(n):
    digit_index = 1
    """ while n > the number of digits contributed by all numbers with 
    digit_index digits. """
    while n > 9 * digit_index * (10 ** (digit_index - 1)):
        """ adjust the number of digits in this range by subtracting the count of 
        digits, and incrementing digit_index to move to the next range. """
        n -= 9 * digit_index * (10 ** (digit_index - 1))
        digit_index += 1

    """ the specific number in the sequence where n falls. """
    number = (n - 1) // digit_index + 10 ** (digit_index - 1)
    position_in_number = (n - 1) % digit_index
    return int(str(number)[position_in_number])

def champernownes_constant(n):
    """ functools.reduce() applies a function to all elements in a list;
    operator.mul returns the product of the given arguments. """
    return functools.reduce(operator.mul, [_find_digit(10 ** i) for i in range(n)])

if __name__ == "__main__":
    print(champernownes_constant(7))
