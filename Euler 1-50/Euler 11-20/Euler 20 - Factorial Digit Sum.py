""" calculates the sum of digits in 'n!' """
def fac(n):
    if n <= 1:
        return 1
    """ as used in #15 """
    return n * fac(n-1)

def countDigits(n):
    factorial = fac(n)
    digit_sum = 0
    for digit in str(factorial):
        """ increments counter w/ integer value of each digit's str. equivalent. """
        digit_sum += int(digit)
    return digit_sum

print(countDigits(100))
