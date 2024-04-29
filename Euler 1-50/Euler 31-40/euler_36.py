"""
Double Base Palinromes
------------------------
585 = 10010010012 is palindromic in bases 2 and 10.
Sum all numbers < n which are palindromic in bases 2 and 10.
"""

import math

def _make_base_2_palindrome(n, odd_length):
    result = n
    if odd_length:
        """ remove n's LSB, ensuring that the generated palindrome's 
        length is odd. """
        n >>= 1
    while n > 0:
        """ mirror n and add its LSB to result. """
        result = (result << 1) + (n & 1)
        n >>= 1
    return result

def double_base_palindromes(n):
    sum_palindromes = 0
    for i in range(1, math.isqrt(n)):
        p_odd = _make_base_2_palindrome(i, True)
        p_even = _make_base_2_palindrome(i, False)

        """ generate an odd and even length base 2 palindrome. if either > n, 
        return the current sum. """
        if p_odd >= n and p_even >= n:
            return sum_palindromes

        """ if not, check if it's palindromic in base 10. """
        if _is_palindrome(p_odd) and p_odd < n: # see Python-Project-Euler/Euler 1-50/Euler 1-10/euler_4.py
            sum_palindromes += p_odd
        if _is_palindrome(p_even) and p_even < n:
            sum_palindromes += p_even
    
    return sum_palindromes

if __name__ == "__main__":
    print(double_base_palindromes(1_000_000))
