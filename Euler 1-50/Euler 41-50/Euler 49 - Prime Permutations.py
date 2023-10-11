""" forms all arithmetic sequences of 3 'n'-digit numbers that increase by a constant, are permutations of each other, and are prime. """
from math import sqrt

def isPrime(n):
    """ all primes > 3 are writable as '6k + 1' or '6k - 1', where 'k' is a positive integer. """
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

def getArithmeticSequences(n):
    primes = {}
    for num in range(10 ** (n-1), 10 ** n):
        """ if prime, convert num's digits to a tuple, before sorting and using it as a key to store 'num' in 'primes'. 
        This groups all primes that are permutations of each other. """
        if isPrime(num):
            key = tuple(sorted(str(num)))
            """ '.setdefault()' returns the value of a key if present; else, it's inserted w. 
            The default value into the dictionary. """
            primes.setdefault(key, []).append(num)

    result = []
    for key in primes:
        """ once all primes have been grouped, loop over each key in the dictionary. If the length of the list of values for that 
        key < 3, continue to the next; otherwise, sort and loop over the values, checking for all possible three-term 
        arithmetic sequences that increase by a constant.  """
        if len(primes[key]) < 3:
            continue
        primes[key].sort()
        for i in range(len(primes[key]) - 2):
            """ for each pair of numbers in the list, calculate 'diff' between them and initialise a 'seq' with them. 
            Then, loop over the remaining numbers in the list, checking if each one is 'diff' units > the previous number in 'seq'. """
            for j in range(i+1, len(primes[key]) - 1):
                diff = primes[key][j] - primes[key][i]
                seq = [primes[key][i], primes[key][j]]
                for k in range(j + 1, len(primes[key])):
                    if primes[key][k] - seq[-1] == diff:
                        """ adds it to the sequence. """
                        seq.append(primes[key][k])
                if len(seq) == 3:
                    result.append(seq)

    return result

print(getArithmeticSequences(4))
