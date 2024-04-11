"""
Lexicographic Permutations
------------------------------
A permutation is an ordered arrangement of objects. The lexicographic permutations of 0, 
1 and 2 are: 012   021   102   120   201   210.
Find the nth lexicographic permutation of the digits 0-9.
"""

def lexicographic_permutation(n):
    digits = list(range(10))
    permutation = ""
  
    for i in range(9, -1, -1):
        """ index of the digit in the remaining digits list that corresponds to the 
        current place in the permutation. """
        index = (n - 1) // _factorial(i) # see Python-Project-Euler/Euler 1-50/Euler 11-20/euler_15.py
        """ remove the chosen digit from the list. """
        digit = digits.pop(index)
        permutation += str(digit)
        """ adjust n to represent the position of the next digit. """
        n -= index * _factorial(i)
    return permutation

if __name__ == "__main__":
  print(lexicographic_permutation(1_000_000))
