""" calculates the no. of possible routes, from the top-left to the bottom-right, of an 'm * n' lattice, using only downward and rightward moves. """
def fac(n):
    if n == 0:
        return 1
    """ recursively returns the product of all positive integers up to 'n'. """
    return n * fac(n-1)

""" total moves required = 'm + n - 2' (i.e. 'm - 1' rightward and 'n - 1' to reach the bottom-right from the top-left, and one move in each direction is already made at the beginning). """
def countLatticePaths(n):
    n_fac = fac(n)
    """ no. of possible routes = no. of ways to choose 'm - 1' out of a total of 'm + n - 2' moves (i.e. choosing 'm - 1' elements out of a set of 'm + n - 2'); achieved via the binomial coefficient '(n choose k) = n! / (k! * (n - k)!)' to be computed as: """
    return fac(n * 2) // n_fac ** 2

print(countLatticePaths(20))
