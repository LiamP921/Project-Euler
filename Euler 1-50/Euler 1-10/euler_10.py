"""
Summation of Primes
----------------------
The sum of primes < 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of primes < n.
"""

    return np.sum(np.where(primes)[0])

if __name__ == "__main__":
    print(eratosthenes(2_000_000)) # see Python-Recreational-Mathematics/primality/sieves/eratosthenes.py
