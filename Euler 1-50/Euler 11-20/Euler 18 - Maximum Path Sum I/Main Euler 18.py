""" calculates the maximum path sum of adjacent numbers in a triangle from top to bottom. """
def getTriangle(triangle_filename):
    triangle = [[int(number) for number in row.split()]
                for row in open(triangle_filename)]
    return triangle

def maximumPathSum(triangle):
    """ move upwards from the penultimate row """
    for row in range(len(triangle) - 1, 0, -1):
        """ for each number, find the two numbers in the below row that are both directly below and adjacent. """
        for col in range(len(triangle[row]) - 1):
            """ adds the maximum of these two numbers to the current number in the row, effectively replacing it w/ the sum. """
            maximum = max(triangle[row][col], triangle[row][col + 1])
            triangle[row - 1][col] += maximum
    """ when it reaches the top, return the single number in that row, representing the MPS. """
    return triangle[0][0]
  
triangle = getTriangle("Triangle.txt")
print(maximumPathSum(triangle))
