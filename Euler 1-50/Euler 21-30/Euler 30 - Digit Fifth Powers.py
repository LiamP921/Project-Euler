""" calculates the sum of all numbers writable as the sum of 'nth' powers of their digits. """
def digitPowersSum(n):
    """ dictionary stores the 'nth' power of each digit 0-9. """
    powers = {i: pow(i, n) for i in range(10)}
    sum_nums = 0
    """ smallest solution is '2', w/ a digit power sum of '2^n'. Largest solution is '9^n * (n + 1)', w/ a DPS of '(n + 1) * 9^n'. """
    for i in range(2, (n + 1) * pow(9, n)):
        temp_sum = 0
        num = i
        while num > 0:
            digit = num % 10
            temp_sum += powers[digit]
            num //= 10
        if temp_sum == i:
            sum_nums += i
    return sum_nums

print(digitPowersSum(5)) 
