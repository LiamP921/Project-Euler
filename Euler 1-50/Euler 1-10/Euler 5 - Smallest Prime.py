""" finds smallest positive value that's evenly divisible by all numbers 1-20. """
def LCM():
  primes = [2,3,5,7,11,13,17,19]
  prod = 1 
  for p in primes:
    n = 2
    prod *= p
    while (p**n < 21):
        prod *= p
        n += 1
  print(prod)

LCM()
