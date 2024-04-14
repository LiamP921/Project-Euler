"""
Digit Factorials
------------------
145 is curious, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Sum all the numbers equal to the sum of the factorial of their digits.
"""

"""
any n-digit number is at most n * 9!. For numbers with >= 8 digits, n * 9! > 10^n. 
This means that any number with >= 8 digits will be too large to be expressed as the 
sum of the factorials of its digits. Thus, only numbers with 1 <= n <= 7 are considered.
"""

def digit_factorial():
    factorials = {i: _factorial(i) for i in range(10)} # see Python-Project-Euler/Euler 1-50/Euler 11-20/euler_15.py
    sum_nums = 0

    for i in range(3, 99999):
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
