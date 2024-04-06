"""
Summation of Primes
----------------------
The sum of primes < 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of primes < n.
"""

if __name__ == "__main__":
    print(sum(eratosthenes(2_000_000))) # see Python-Recreational-Mathematics/primality/sieves/eratosthenes.py
