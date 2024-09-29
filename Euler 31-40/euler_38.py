""" Pandigital Multiples
----------------------------
192384576 represents the concatenated product of 192 and (1, 2, 3).
Find the largest 1 to k pandigital k-digit number formable as the concatenated 
product of an integer with (1, 2, ..., n) where n > 1, and 8 <= k <= 9. """

def pandigital_multiples(k):
    digits = set("1234567890"[:k])
    largest_pandigital = 0
    """ integers > 9876 produce a concatenated product > 9 digits. """
    for n in range(2, 9876):
        p = str(n)
        """ multipliers ensure that the concatenated product remains within k 
        digits. """
        for j in [2, 3, 4, 5]:
            p = "".join([p, str(n * j)])
            if len(p) == k and set(p) == digits:
                """ max() returns the largest item in an iterable or in two or 
                more arguments. """
                largest_pandigital = max(largest_pandigital, int(p))
    return largest_pandigital

if __name__ == "__main__":
    print(pandigital_multiples(9))
