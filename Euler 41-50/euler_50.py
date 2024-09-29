""" Consecutive Prime Sum
-----------------------------
The longest sum of consecutive primes below one-thousand that adds to a 
prime, contains 21 terms, and is equal to 953.

Calculate the prime < n writable as the sum of the most consecutive primes. """

def _prime_sum_below_n(n):
    primes = []
    sum_primes = 0
    i = 2
    """ generate primes consecutively until their sum > n """
    while sum_primes + i <= n:
        if _miller_rabin(i): # see Recreational-Algorithms/number_theory/miller_rabin.py
            primes.append(i)
            sum_primes += i
        i += 1
    return primes

def consecutive_prime_sum(n):
    primes = _prime_sum_below_n(n)
    max_primes = len(primes)
    """ starting at the maximum, iterate over all possible lengths of consecutive 
    prime sums. """
    for length in range(max_primes, 0, -1):
        """ for each length, slide a window over the list of primes and sum those 
        it contains. """
        for i in range(max_primes - length + 1):
            sum_primes = sum(primes[i:i+length])
            if _miller_rabin(sum_primes):
                return sum_primes

if __name__ == "__main__":
    print(consecutive_prime_sum(1_000_000))
