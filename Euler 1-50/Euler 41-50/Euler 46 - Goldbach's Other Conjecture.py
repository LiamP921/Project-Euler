""" calculates the smallest odd composite that can't be written as the sum of a prime and twice a square (i.e. in the form 
'c = p + 2n^2'). """
from math import sqrt

""" alteration of #41's prime sieve, using how all primes > 3 are writable as '6k + 1' or '6k - 1', where 'k' is 
a positive integer. """
def isPrime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    """ only need to check if 'n' is divisible by primes of the aforementioned forms up to the 'sqrt(n)'. """
    while i <= int(sqrt(n)):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def smallestOddComposite():
    """ first odd composite. """
    n = 9
    while True:
        if not isPrime(n):
            found = False
            for i in range(int(sqrt(n / 2)) + 1):
                if isPrime(n - 2 * i * i):
                    found = True
            if not found:
                return n
        n += 2

print(smallestOddComposite())
