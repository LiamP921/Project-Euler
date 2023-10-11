""" calculates the denominator of the product of the four non-trivial fractions < '1' w/ two-digit numerators and denominators, in its lowest common terms. """
from fractions import Fraction
from math import gcd

""" trivial numerators and denominators have a common factor > '1'; therefore, non-trivials will be coprime (i.e. have no common factors besides '1'). """
def nonTrivialDenominator():
    """ non-trivial fractions: '16/64 = 1/4', '19/95 = 1/5', '26/65 = 2/5', '49/98 = 1/2'; 'Fraction' constructs instances from integer arguments. """
    non_trivial_fractions = [Fraction(16, 64), Fraction(19, 95), Fraction(26, 65), Fraction(49, 98)]
    numerator_product = 1
    denominator_product = 1

    for fraction in non_trivial_fractions:
        numerator_product *= fraction.numerator
        denominator_product *= fraction.denominator
    """ 'gcd' computes the greatest common divisor (HCF) of two arguments. """
    common_divisor = gcd(numerator_product, denominator_product)
    return denominator_product // common_divisor

print(nonTrivialDenominator())
