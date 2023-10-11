""" calculates the product of the first 'n' digits in the 'dn' sequence of concatenated positive integers. """
def getDigit(n):
    """ find the smallest 'k' such that the total number of digits used to represent numbers '1 to k' is '>= n'. """
    k = 1
    while n > 9 * k * 10 ** (k - 1):
        """ decreased by the number of digits needed to represent the current '1 to k' range. """
        n -= 9 * k * 10 ** (k - 1)
        k += 1

    """ determine which number 'dn' belongs to for a given 'n'. """
    num = 10 ** (k - 1) + (n - 1) // k
    """ get the position of 'dn' within the number. """
    pos = (n - 1) % k
  
    return int(str(num)[pos])

digit_prod = getDigit(1) * getDigit(10) * getDigit(100) * getDigit(1000) * getDigit(10000) * getDigit(100000) * getDigit(1000000)
print(digit_prod)
