""" calculates the product of a Pythagorean triplet (set of three naturals, for which which,'a^2 + b^2 = c^2') which sums to 't'. """
from math import sqrt

def pythagoreanTripletProduct(t):
    for m in range(int(sqrt(t) / 2), int(sqrt(t / 2))):
        n = t / (2 * m) - m

        """ Euclid's Pythagorean triplet generating formula: """
        if m > n > 0 and n.is_integer():
            a = 2 * m * n 
            b = m * m - n * n
            c = m * m + n * n

            return int(a * b * c)

print(pythagoreanTripletProduct(1000))
