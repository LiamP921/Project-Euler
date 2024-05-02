"""
Sub-String Divisibility
------------------------
With 1406357289, let d1 and d2 be the 1st and 2nd digit, and so on. In this way, note 
the following: d2d3d4 = 406 is divisible by 2, d3d4d5 = 063 by 3, d4d5d6 = 635 by 5, 
d5d6d7 = 357 by 7, d6d7d8=572 by 11, d7d8d9 = 728 by 13, d8d9d10 = 289 by 17.

Sum all the 0-n pandigitals with sub-strings with this property.
"""

def _sum_pandigitals(digits_left, current, current_length, primes):
    if len(digits_left) == 0:
        return int(current)
    else:
        """ iterate over the remaining digits and attempt to add each to the current 
        pandigital. """
        total_sum = 0
        for i in range(len(digits_left)):
            digit = digits_left.pop(i)
            current += digit
            current_length += 1
            """ if the length of the current pandigital < 4 or if the last three digits form 
            a substring divisible by the corresponding prime. Only consider the last three pandigital digits, 
            as the largest prime, 17, corresponds to a 3-digit substring. """
            if current_length < 4 or int(current[current_length - 3 : current_length]) % primes[current_length - 4] == 0:
                total_sum += _sum_pandigitals(digits_left, current, current_length, primes)
            """ after each iteration, remove the last added digit to backtrack, 
            ensuring all combinations are explored. """
            current = current[:-1]
            current_length -= 1
            """ .insert() inserts an item into a list at a specified index. """
            digits_left.insert(i, digit)
        return total_sum

def substring_divisibility(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    digits = [str(i) for i in range(n + 1)]
    return _sum_pandigitals(digits, "", 0, primes)

if __name__ == "__main__":
    print(substring_divisibility(9))
