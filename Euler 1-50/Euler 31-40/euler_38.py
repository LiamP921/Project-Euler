"""
Pandigital Multiples
-----------------------
192384576 represents the concatenated product of 192 and (1, 2, 3).

Find the largest 1 to k pandigital k-digit number formable as the concatenated 
product of an integer with (1, 2, ..., n) where n > 1.
"""

def pandigital_multiples(k):
    digits = set("123456789"[:k])
    largest_pandigital = 0
    """ concatenate numbers > 9876 with consecutive multipliers from 
    1-n > a 9-digit number. """
    for integer in range(9876):
        concatenated_product = ""
        multiplier = 1
        while len(concatenated_product) < k:
            concatenated_product = "".join([concatenated_product, str(integer * multiplier)])
            multiplier += 1
        if len(concatenated_product) == k and set(concatenated_product) == digits:
            """ max() returns the largest item in an iterable or in two or 
            more arguments. """
            largest_pandigital = max(largest_pandigital, int(concatenated_product))
    return largest_pandigital

if __name__ == "__main__":
    print(pandigital_multiples(9))
