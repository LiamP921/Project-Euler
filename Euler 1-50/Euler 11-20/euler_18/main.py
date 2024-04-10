"""
Maximum Path Sum I
---------------------
Starting at the top of the triangle below and moving to adjacent numbers on the row 
below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
Find the maximum total from top to bottom for the given triangle.
"""

def maximum_path_sum():
    with open("triangle.txt", "r") as file:
        triangle = [[int(number) for number in row.split()] for row in file]

    """ move upwards from the penultimate row. """
    for row in range(len(triangle) - 2, -1, -1):
    """ for each number, find the two numbers in the row below that are both directly 
    below and adjacent. """
        for col in range(len(triangle[row])):
            """ add the maximum of these two numbers to the current number in the row, 
            effectively replacing it w/ the sum. """
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    """ upon reaching the top, return the single number in that row, 
    representing the maximum path sum. """
    return triangle[0][0]

if __name__ == "__main__":
    print(maximum_path_sum())
