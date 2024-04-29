"""
Summation of Primes
----------------------
The sum of primes < 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of primes < n.
"""

    return np.sum(np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)])

if __name__ == "__main__":
  print(eratosthenes(2_000_000)) # see Python-Recreational-Mathematics/primality/sieves/eratosthenes.py
