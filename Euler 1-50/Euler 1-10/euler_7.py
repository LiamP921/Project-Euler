"""
10001st Prime
-----------------
By listing the first six primes (2, 3, 5, 7, 11, and 13), 13 is the 6th.
Find the nth prime.
"""

def nth_prime(n):
    """ prime number theorem states that the nth prime ~= n nlog(n). This is an 
    asymptotic approximation, becoming more accurate as n grows. For greater 
    precision, incorporate log(log(n)) to adjust for the increasing gap between 
    consecutive primes. """
    return _eratosthenes(math.ceil(n * (math.log(n) + math.log(math.log(n)))))[n - 1] # see Python-Recreational-Mathematics/primality/sieves/eratosthenes.py

if __name__ == "__main__":
  print(nth_prime(10001))
