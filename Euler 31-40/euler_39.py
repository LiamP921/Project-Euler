"""Integer Right Triangles
---------------------------------
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120: {20,48,52}, {24,45,51}, {30,40,50}

Find the value of p ≤ n, of which the number of solutions maximized. """

""" 1). Substituting Euclid's formula into p = a + b + c gives (m^2 - n^2) + 2mn + 
(m^2 + n^2) = 2mn + 2mn = 2m(m + n).

2). The search space can be further optimised via an upper bound for m based on the 
limit: p = 2m(m + n) <= 1000m(m + n) <= 500m^2 + mn <= 500. Since m > n, the maximum 
m can be assumed to occur when n = 1. Therefore, m^2 + m <= 500 ~ sqrt(500).

3). All possible combinations of m and n can now be iterated over with m^2 <= 500, 
m > n, and m - 1 ≡ (mod 2) to find the p that maximizes the number of integer solutions 
{a,b,c}. """

import math

def integer_right_triangles(n):
    max_length = math.isqrt(n // 2) + 1
    solution_counts = [0] * (n + 1)

    for first_length in range(2, max_length):
        for second_length in range(1, first_length):
            if (first_length - second_length) % 2 == 1 and _greatest_common_divisor(first_length, second_length) == 1: # see Project-Euler/Euler 1-10/euler_5.py
                perimeter = 2 * first_length * (first_length + second_length)
                for perimeter_value in range(perimeter, n + 1, perimeter):
                    solution_counts[perimeter_value] += 1

    max_solutions = 0
    max_perimeter = 0

    for perimeter_value in range(1, n + 1):
        if solution_counts[perimeter_value] > max_solutions:
            max_solutions = solution_counts[perimeter_value]
            max_perimeter = perimeter_value

    return max_perimeter

if __name__ == "__main__":
    print(integer_right_triangles(1000))
