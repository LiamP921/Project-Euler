"""
Multiples of 3 or 5
-----------------------
3, 5, 6 and 9 are all the natural multiples of 3 or 5 < 10; these sum to 23.
Find the sum of all the multiples of 3 or 5 < num.
"""

"""
1a). Gauss summation formula: n∑i=1 = (1/2)(n(n + 1)). Multiples of 3 are 
3,6,9,12... Placing 3 outside the brackets gives 3⋅(1,2,3,4,...). Thus, the 
amount of numbers needed to be summated is [n/3]

1b). Finding it for a general k and calculating the sum of multiples requires: 
σ(n,k) = k [n/k]∑i=1 i = (k/2)[n/k]([n/k] + 1).

2). σ(999,3) + σ(999,5) presents a problem: all numbers divisible by 3 and 5 are 
counted twice. As lcm(5,3) = 15, all multiples of 15 must be subtracted: σ(999,3) 
+ σ(999,5) − σ(999,15).
"""

def multiples_of_3_or_5(n):
    r = (n - 1) // 3
    s = (n - 1) // 5
    t = (n - 1) // 15
  
    return 3 * r * (r + 1) + 5 * s * (s + 1) - 15 * t * (t + 1) >> 1

if __name__ == "__main__":
  print(multiples_of_3_or_5(1000))
