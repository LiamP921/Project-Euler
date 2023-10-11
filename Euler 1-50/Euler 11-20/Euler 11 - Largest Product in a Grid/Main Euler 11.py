""" calculates greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in an 
'n x n' grid """
import numpy as np

n = 20
""" loads numerical data; 'dtype' loads grid as an integer matrix """
grid = np.loadtxt("Grid.txt", dtype="i")

""" iterates over each row of the grid; then iterates over each four-element subsequence to the right. """
def getRight(grid):
    all_products = []
    for i in range(n):
        for j in range(n - 3):
            four_elements = grid[i, j:j+4]
            """ 'prod' returns product of elements over a given axis """
            all_products.append(np.prod(four_elements))
    return max(all_products)

""" reverses the order of elements row-wise (calculates max product of four-element subsequence to the left
via reversed column order). """
def getLeft(grid):
    return getRight(np.fliplr(grid))

""" rotates matrix 90 degrees counter-clockwise (calculates maximum product of four-element subsequence downwards). """
def getDown(grid):
    return getRight(np.rot90(grid))

""" iterates over all diagonals that start in the top half and end in the bottom half. """
def getDiag1(grid):
    all_products = []
    for i in range(-n+1, n):
        dgnl = np.diagonal(grid, i)
        for start in range(len(dgnl) - 3):
            four_elements = dgnl[start:start+4]
            all_products.append(np.prod(four_elements))
    return max(all_products)

""" reverses the order of elements row-wise (calculates maximum product of four-element subsequence along opposite diagonal). """
def getDiag2(grid):
    flipped = np.fliplr(grid)
    all_products = []
    for i in range(-n+1, n):
        dgnl = np.diagonal(flipped, i)
        for start in range(len(dgnl) - 3):
            four_elements = dgnl[start:start+4]
            all_products.append(np.prod(four_elements))
    return max(all_products)

max_product = max(getRight(grid), getLeft(grid), getDown(grid), getDiag1(grid), getDiag2(grid))
print(max_product)
