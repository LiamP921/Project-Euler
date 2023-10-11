""" calculates the sum of diagonals in an 'n * n' spiral-square matrix. """
def ssMatrixDiagonalsSum(n):
    """ four corners' sum is '4 * sum of odds from 1 to 'n - 1'. As the corners are always at (1, 1), (1, n), (n, 1), and (n, n), the formula is: '4 * (n - 1) ** 2.' """  
    return (4 * n ** 3 + 3 * n ** 2 + 8 * n - 9) // 6
""" summation of separate diagonals can be thought of in two parts, where the first has starting and last numbers '1' and '1 + (n // 2)(n - 1)'. The second, whereas, has starting and last numbers 'n ** 2' and 'n ** 2 - (n // 2)(n - 1)'. """
print(ssMatrixDiagonalsSum(1001))
""" the summation of an arithmetic series formula then gives the final respective expressions of '(n // 2)(2 + (n // 2 - 1)(n - 1))', and '(n // 2)(2n ** 2 - (n // 2 + 1)(n - 1))', to be summed together and alongside the four corners' sum formula. The result is then finally, simplified into the above expression. """
