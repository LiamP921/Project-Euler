"""
Largest Product in a Grid
---------------------------
In the given 20×20 grid, the diagonal 26, 63, 78, 14 has a product of 1788696.
Calculate the greatest product of n adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the given grid.
"""

import numpy as np

def largest_grid_product(n):
    grid = np.loadtxt("grid.txt", dtype=int)
    """ np.shape() returns a tuple of elements containing the lengths of the corresponding
    array dimension. """
    (y, x) = np.shape(grid)
    max_product = 0

    for i in range(y): # horizontal
        for j in range(x - n + 1):
            """ for each row, slide an n-sized window across it to find all possible 
            horizontal sequences; np.prod() returns the product array elements of a 
            given axis. """
            product = np.prod(grid[i, j:j + n])
            if product > max_product:
                max_product = product

    for i in range(x): # vertical
        for j in range(y - n + 1):
            product = np.prod(grid[j:j + n, i])
            if product > max_product:
                max_product = product

    for i in range(y - n + 1): # left-to-right diagonal
        for j in range(x - n + 1):
            """ np.diag() creates a new ndarray with the given 1D array as its diagonal 
            elements, or extracts the diagonal from the given ndarray. """
            product = np.prod(np.diagonal(grid[i:i + n, j:j + n]))
            if product > max_product:
                max_product = product

    for i in range(y - n + 1): # right-to-left diagonal
        for j in range(n - 1, x):
            """ np.fliplr flips a 2d array in a left-right direction; columns are preserved, 
            but appear in a different order. """
            product = np.prod(np.diagonal(np.fliplr(grid[i:i + n, j - n + 1:j + 1])))
            if product > max_product:
                max_product = product
    return max_product

if __name__ == "__main__":
    print(largest_grid_product(4))
