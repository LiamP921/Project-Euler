""" calculates the sum of all positive integers which can't be written as the sum of two abundant numbers (whose proper divisor sum is > than said number). """
from math import ceil

def sumDivisors(n):
    if n == 1: 
      return 0
    sum_div = 1
    """ 'ceil' returns smallest integer >= 'x'.  """
    sqrt = ceil(n ** 0.5)
    for i in range(2, sqrt):
        if n % i == 0:
            """ divisors of 'n', including the quotient, are summed, as per #21. """
            sum_div += (i + n // i)
    return sum_div + (sqrt if sqrt ** 2 == n else 0) 

""" 'set' utilised to separate amicable sums by holding multiple elements; unlike arrays, element order is undefined, allowing for faster presence checking. """
abundants = set()
non_abundants_sum = 0
""" all integers > 28123 can be written as the sum of two abundants. """
for i in range(1, 28123 + 1):
    """ if number is expressible as the sum of two elements in 'abundants'. """
    if not any(i - a in abundants for a in abundants):
        non_abundants_sum += i
    if sumDivisors(i) > i:
        abundants.add(i)
print(non_abundants_sum)
