"""
Double Base Palinromes
------------------------
585 = 10010010012 (binary) is palindromic in both bases.
Sum all numbers < n which are palindromic in bases 10 and 2.
"""

import math

def _is_palindrome(n, base):
    reversed_num = 0
    k = n
    while k > 0:
        reversed_num = base * reversed_num + k % base
        k //= base # modified from Python-Project-Euler/Euler 1-50/Euler 1-10/euler_4.py to work for any given base.
    return n == reversed_num

def _make_base_2_palindrome(n, odd_length):
    result = n
    if odd_length:
        """ remove n's LSB, ensuring that the enerated palindrome's 
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
        returns the current sum of palindromes. """
        if p_odd >= n and p_even >= n:
            return sum_palindromes

        """ if not, check if it's palindromic in base 10. """
        if _is_palindrome(p_odd, 10) and p_odd < n:
            sum_palindromes += p_odd
        if _is_palindrome(p_even, 10) and p_even < n:
            sum_palindromes += p_even
    
    return sum_palindromes

if __name__ == "__main__":
    print(double_base_palindromes(1_000_000))
