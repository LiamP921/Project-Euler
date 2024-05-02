"""
Digit Factorials
------------------
145 is curious, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Sum all the numbers equal to the sum of the factorial of their digits.
"""

"""
1). For numbers with >= 8 digits, n * 9! > 10^n, making them too large to be 
expressed as the sum of the factorials of its digits. Thus, only numbers with 
1 <= n <= 7 are considered.

2). The factorial of any odd/even number contains no/at least one factor of 2. 
Since the sum of factorials will consist of the sum of individual ones, if 
any of the digits are odd, the sum will be too. 
"""

def digit_factorial():
    """ precompute factorial for each digit. """
    factorials = {i: _factorial(i) for i in range(10)} # see Python-Project-Euler/Euler 1-50/Euler 11-20/euler_15.py
    sum_nums = 0

    for i in range(10, 99999, 3):
        temp_sum = 0
        num = i
        while num > 0:
            digit = num % 10
            temp_sum += factorials[digit]
            num //= 10
        if temp_sum == i:
            sum_nums += i
    return sum_nums

if __name__ == "__main__":
    print(digit_factorial())
