"""
Non-Abundant Sums
---------------------
A perfect/abundant/deficient number's proper divisor sum is ==/</> than said number. 
As 12 is the smallest abundant number, 24 is the smallest number that can be written as 
the sum of two abundants. All integers > 28123 can be written as the sum of two abundants. 
However, this upper limit can't be reduced any further by analysis, even though the greatest 
number that can't be expressed as the sum of two abundants is < this limit.

Sum all the positive integers <= limit which can't be written as the sum of two abundants.
"""

def non_abundant_sums(limit):
    sum_divisors = _proper_divisor_sums(limit) # see Python-Project-Euler/Euler 1-50/Euler 21-30/euler_21.py
    result = 0
    abundants = set()
    """ n's sum of proper divisors > n, add it to the set of abundants. """
    for n in range(1, limit + 1):
        if sum_divisors[n] > n: 
            abundants.add(n)
        """ if there are no abundants a such that n - a is also abundant, adds n 
        to the result. """
        if not any((n - a in abundants) for a in abundants): 
            result += n
    return result

if __name__ == "__main__":
    """ largest number which can't be written as the sum of two abundants. """
    print(non_abundant_sum(20161))
