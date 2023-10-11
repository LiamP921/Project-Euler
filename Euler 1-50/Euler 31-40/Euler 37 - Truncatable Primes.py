""" calculate the sum of the eleven primes truncatable from left to right, and vice versa.  """
def sieveOfEratosthenes(n):
    primes = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, n + 1) if primes[i]]

def isTruncatablePrime(n, primes_set):
    """ single digits aren't truncatable. """
    if n < 10 or n not in primes_set:
        return False
      
    s = str(n)
    for i in range(1, len(s)):
        """ each position 'i' is membership checked. """
        if int(s[i:]) not in primes_set or int(s[:-i]) not in primes_set:
            return False  
    return True

def countTruncatablePrime(limit):
    primes = sieveOfEratosthenes(limit)
    primes_set = set(primes)
    truncatable_sum = 0
    for p in primes:
        if isTruncatablePrime(p, primes_set):
            truncatable_sum += p
    return truncatable_sum
  
""" arbitrary limit, as per #36. """
print(countTruncatablePrime(1000000))
