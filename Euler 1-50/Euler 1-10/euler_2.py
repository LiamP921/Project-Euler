"""
Even Fibonacci Numbers
--------------------------
Each Fibonacci term is generated by adding the previous two. Starting for 1 and 2, the first 10 are: 1, 2, 3, 5, 8, 13, 
21, 34, 55, 89, ...
Find the sum of the even terms whose value doesn't exceed n.
"""

import math

def nth_fibonacci(n):
    """ for quantities a and b with a > b > 0, a is in a golden ratio to 
    b if (a + b) / a = a / b = φ. """
    phi = (1 + math.sqrt(5)) / 2
    """ Binet's formula. """
    return int((phi ** n - (-1 / phi) ** n) / math.sqrt(5))

def even_fibonacci_sum(limit):
    sum_fibonacci = 0
    i = 3
    while True:
        fib_i = nth_fibonacci(i)
        """ if the calculated Fibonacci > limit. If so, returns the sum of even 
        Fibonaccis calculated so far. """
        if fib_i > limit:
            return sum_fibonacci
        sum_fibonacci += fib_i
        """ every third Fibonacci is even. """
        i += 3

if __name__ == "__main__":
    print(even_fibonacci_sum(4_000_000))
