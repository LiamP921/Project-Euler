"""
Multiples of 3 or 5
-----------------------
3, 5, 6 and 9 are all the natural multiples of 3 or 5 < 10; these sum to 23.
Find the sum of all the multiples of 3 or 5 < num.
"""

def multiples_of_3_or_5(num):
  num -= 1 
  def _sum_divisible_by(n):
      p = number // n
      return n * (p * (p + 1)) // 2
      """ subtracted as 'sumDivisibleBy(15)' was previously found via '3' and '5'. """
  return _sum_divisible_by(3) + _sum_divisible_by(5) - _sum_divisible_by(15)

print(multiples_of_3_or_5(1000))
