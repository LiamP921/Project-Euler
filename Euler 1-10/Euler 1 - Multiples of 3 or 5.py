""" finds sum of all multiples of 3 or 5 below 1000 """
def sumDivisibleBy(n):
    targ = 999
    p = targ // n 
    return n * (p * (p + 1)) // 2
""" subtracted as 'sumDivisibleBy(15)' was previously found via '3' and '5'. """
print(sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))
