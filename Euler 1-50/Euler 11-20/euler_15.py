"""
Lattice Paths
----------------
Starting in the top left corner of a 2×2 grid, and only being able to move to the right 
and down, there are exactly 6 routes to the bottom right.
Calculate how many such routes there are in an n * n grid.

1). Each lattice path corresponds to a unique combination of moving right (x) and up (y). The number 
of lattice paths to reach a point (x,y) is the coefficient of x^x or y^y in the expansion of (x + y)^x+y, 
which is equivalent to (x + y)^2x or (x + y)^2y.

2). Thus, to count the number of lattice paths from the origin to the farthest point on the grid (a x a), 
calculate the coefficient of (x + y)^2a.

3). This is achieved by calculating the binomial coefficient (2a choose a) via 2a! / (a! * (2a - a)!). 
This represents the number of ways to choose a items (movements) from a total set of 2a.
"""

def factorial(n):
    fac = 1
    for i in range(2, n + 1):
        fac *= i
    return fac

def count_lattice_paths(n):
    return factorial(n * 2) // factorial(n) ** 2

if __name__ == "__main__":
    print(count_lattice_paths(20))
