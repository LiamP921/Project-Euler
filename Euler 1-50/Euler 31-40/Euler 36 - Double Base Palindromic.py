""" calculates the sum of values < 'n' which are palindromic in both base 2 and 10. """
def isPalindromic(n):
    """ checks if a given integer is palindromic, as per #4. """
    return str(n) == str(n)[::-1]

def sumDualBasePalindromic(n):
    elem_sum = 0
    for i in range(1, n):
        """ 'bin' returns an integer's equivalent binary string."""
        if isPalindromic(i) and isPalindromic(bin(i)[2:]):
            elem_sum += i
    return elem_sum

print(sumDualBasePalindromic(1000000))
