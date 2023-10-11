""" calculates the sum of digits of 'n^m'. """
def sumOfPowerDigits(n, m):
    num = n ** m
    digits = list(str(num))
    digit_sum = sum(int(d) for d in digits)
    return digit_sum

print(sumOfPowerDigits(2, 1000))
