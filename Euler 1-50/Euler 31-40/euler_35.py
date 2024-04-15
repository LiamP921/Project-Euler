"""
Circular Primes
-----------------
197 is a circular prime, as all rotations of its digits  (197, 971, and 719) are 
also prime.
Calculate the number of circular primes < n.
"""

def is_circular(number):
    num_digits = len(str(number))
    for _ in range(num_digits):
        if not _miller_rabin(number): # see Python-Recreational-Mathematics/primality/miller_rabin.py
            return False
        else:
            """ rotate number by moving the last digit to the first position. """
            last_digit = number % 10
            remaining_digits = number // 10
            number = (last_digit * (10 ** (num_digits - 1))) + remaining_digits
    return True

def circular_primes(n):
    count = 2
    """ a circular prime can only consist of combinations of 1, 3, 7 or 9, as having 0, 
    2, 4, 6 or 8 as the last digit makes the number divisible by 2, whilst 0 or 5 makes 
    it divisible by 5. """
    digits = "1379"
    for i in range(1, len(str(n)) + 1):
        """ itertools.product() returns the Cartesian Product of an iterable  
        (the set of all ordered pairs (a, b)) with itself for the number of times 
        specified by repeat """
        for rotation in itertools.product(digits, repeat=i):
            number = int("".join(rotation))
            if number < n and is_circular(number):
                count += 1
    return count
  
if __name__ == "__main__":
    print(circular_primes(1_000_000))
