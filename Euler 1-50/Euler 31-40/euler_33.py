"""
Digit Cancelling Fractions
---------------------------------
One may incorrectly believe that 49/98 = 4/8 is obtained by cancelling the 9s. 
Consider fractions like 30/50 = 3/5 to be trivial examples. There are four 
non-trivial examples of this type of fraction, less than one in value and with two 
digit numerators and denominators.

If the product of these four is given in its lowest common terms, find the value of the denominator.
"""

def digit_cancelling_fractions():
    product_numerator = 1
    product_denominator = 1

    for first_digit in range(1, 10):
        numerator_candidate = 9 * first_digit ** 2
        denominator_candidate = 9 * first_digit
        """ restrict the range of the second digit to avoid duplicates and keep 
        fractions < 1. """
        limit = 100 * first_digit // (9 * first_digit + 10)

        """ for each digit combination, update the numerator and denominator 
        candidates. """
        for other_digit in range(first_digit + 1, limit + 1):
            """ generate different combinations of two digit number """
            numerator_candidate += 9 * first_digit
            denominator_candidate -= 1
            """ if the numerator candidate is divisible by the denominator candidate, 
            a digit-cancelling fraction is found. """
            if numerator_candidate % denominator_candidate == 0:
                product_numerator *= first_digit
                product_denominator *= other_digit
    return product_denominator // product_numerator

if __name__ == "__main__":
    print(digit_cancelling_fractions())
