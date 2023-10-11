""" calculates the the first 'n' consecutive integers to have 'k' distinct prime factors each. """
def primeFactorisation(n):
    spf = [0] * (n + 1)
    primes = []
    for i in range(2, int(n ** 0.5) + 1, 2):
        """ adaptation of #35's SOE, where each element 'spf[i]' is the smallest prime factor of 'i'; all evens are 
        initialised to have 'spf[i] = 2'. """
        spf[i] = 2
    primes.append(2)
    """ iterate over odds from 3; if 'i' is prime, set 'spf[i] = i', append 'i' to 'primes', and update all multiples of 
    'i' in 'spf' to be 'i'. """
    for i in range(3, n + 1, 2):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            for j in range(i * i, n + 1, 2 * i):
                if spf[j] == 0:
                    spf[j] = i
    return primes

def distinctPrimeFactors(n, primes):
    count = 0
    i = 0
    sqrt_n = int(n ** 0.5)

    """ iterate over 'primes' up to 'sqrt_n', counting each PF of 'n' and dividing 'n' by that PF until it's no longer a factor. """
    while primes[i] <= sqrt_n:
        if n % primes[i] == 0:
            count += 1
            while n % primes[i] == 0:
                n //= primes[i]
            sqrt_n = int(n ** 0.5)
        i += 1

    if n > 1:
        count += 1

    return count

""" parameters for general 'n' consecutives w/ 'k' distinct PFs. """
def consecutiveIntegers(n, k):
    primes = primeFactorisation(1000000)
    i = 2
    count = 0
    found = True
    window = []

    while found:
        if len(window) < n:
            """ if 'i' has 'k' distinct PFs, append it to 'window' and increment count. """
            if distinctPrimeFactors(i, primes) == k:
                window.append(i)
                count += 1
                """ if 'count' becomes equal to 'n', terminate loop; if 'i' doesn't have 'k' distinct PFs, reset 'window' and 'count'. """
                if count == n:
                    found = False
            else:
                window = []
                count = 0
  
        else:
            """ when loop count becomes equal to 'n', check if 'i' has 'k' distinct PFs. If so, remove the first element of 'window' and append 'i' to the end. """
            if distinctPrimeFactors(i, primes) == k:
                window.pop(0)
                window.append(i)
            else:
                """ 'window' tracks a sliding window of 'n' consecutive integers w/ 'k' distinct PFs. """
                window = []
                count = 0
        i += 1

    return window

print(consecutiveIntegers(4, 4))
