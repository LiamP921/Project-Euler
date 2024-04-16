"""
Pandigital Multiples
-----------------------
192384576 represents the concatenated product of 192 and (1, 2, 3).

Find the largest 1 to k pandigital k-digit number formable as the concatenated 
product of an integer with (1, 2, ..., n) where n > 1.
"""

def _is_pandigital(number):
    digit_mask = 0
    digit_count = 0
    while number > 0:
        """ take the last digit of the number, and set the corresponding bit in 
        digit_mask by ORing it with 1 shifted left by that digit. """
        digit_mask |= 1 << (number % 10)
        number //= 10
        """ number is pandigital if the bitwise OR of digit_mask and 2 equals a value 
        that represents a sequence of 1s followed by digit_count number of 0s 
        (effectively checking if all digits from 1 to digit_count appear exactly once). 
        """
        digit_count += 1
    return 2 + digit_mask == 1 << (digit_count + 1)

def pandigital_multiples(k):
    largest_pandigital = 0
    for integer in range(9876, 1, -1):
        concatenated_product = ""
        multiplier = 1
        while len(concatenated_product) < k:
            """ the concatenation of numbers > 9876 with consecutive multipliers from 
            1-n > a 9-digit number. """
            concatenated_product += str(integer * multiplier)
            multiplier += 1
        if len(concatenated_product) == k and _is_pandigital(int(concatenated_product)):
            """ max() returns the largest item in an iterable or in two or 
            more arguments. """
            largest_pandigital = max(largest_pandigital, int(concatenated_product))
    return largest_pandigital

if __name__ == "__main__":
    print(pandigital_multiples(9))
