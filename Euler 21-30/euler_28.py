"""
Number Spiral Diagonals
--------------------------
Starting from 1 and moving to the right in a clockwise direction forms a 5 * 5 
spiral: 21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13
Sum the numbers on the diagonals in an n * n spiral formed in the same way.
"""

"""
1). As the corners are always at (1, 1), (1, n), (n, 1), and (n, n), they can be 
summed via 4 * (n - 1)^2. 

2). The summation of separate diagonals can be thought of in two parts: the first has 
starting and last numbers 1 and 1 + (n // 2)(n - 1). The second has starting and last 
numbers n^2 and n^2 - (n // 2)(n - 1).

3). The summation of an arithmetic series formula ((n / 2)(a + l), where n is the 
number of terms in the series, and a and l are the first and last terms) can then be 
used to sum the first and second parts of the diagonal via (2 + (n // 2 - 1)(n - 1)) 
and (2n^2 - (n // 2 + 1)(n - 1)).

4). The summation of both parts and all four corners can then be simplified into the 
equation used in the function.
"""

def number_spiral_diagonals(n):
    return (4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) // 6

if __name__ == "__main__":
    print(number_spiral_diagonals(1001))
