"""
Sum Square Difference
-----------------------------
The sum of the squares of the first ten naturals is: 12 + 22 + ... + 102 = 385
The square of the sum of the first ten naturals is: (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of these squares and the square of the sum 
is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first n naturals and the 
square of the sum.
"""

def sum_square_difference(n):
    """
    sum_square_difference = ((n * (n + 1)(2n + 1)) / 6) - (n * (n + 1) / 2) ** 2
    = ((8n ** 3) + (12n ** 2) + 4n - (3n ** 2)((n ** 2) + 2n + 1))) // 12
    = ((8n ** 3) + (12n ** 2) + 4n - (3n ** 4) - (6n ** 3) - (3n ** 3)) // 12 
    = (-(3n ** 4) -(2n ** 3) + (9n ** 2) + 4n) / 12 """
    return (3 * (n ** 4) + 2 * (n ** 3) - 3 * (n ** 2) - 2 * n) // 12

if __name__ == "__main__":
  print(sum_square_difference(100))
