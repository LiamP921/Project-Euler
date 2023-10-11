""" calculates the sum of all numbers equal to the sum of the factorials of their digits. """
def fac(num):
    if num == 0:
        return 1
    """ as used in #15 and #20. """
    return num * fac(num - 1)

def digitFactorialSum():
    """ dictionary stores the 'nth' factorial of each digit, as per #30. """
    factorials = {i: fac(i) for i in range(10)}
    sum_nums = 0
    """ smallest solution is '3', as per the exclusion of non-sums '1!' and '2!'. Largest solution is '99999', as any n-digit number 
    is at most 'n * 9!'. For 'n >= 8', there is 'n * 9! < 10^n', so any n-digit number with 'n >= 8' is too large to be 
    expressed as the DFS of itself. Thus, only numbers with '1 <= n <= 7' are considered. """
    for i in range(3, 99999):
        temp_sum = 0
        num = i
        while num > 0:
            digit = num % 10
            temp_sum += factorials[digit]
            num //= 10
        if temp_sum == i and i > 2:
            sum_nums += i
    return sum_nums

print(digitFactorialSum())
