""" calculates the sum of all products whose multiplicand/multiplier/product identity can be written as a 1-9 pandigital. """
from itertools import product

def isPandigital(n, digits="123456789"):
	return "".join(sorted(str(n))) == digits

products = set()
""" 'product' computes the cartesian product of a variable, as per #29. """
for a, b in product(range(1, 100), range (1, 2000)):
    product = a * b
    """ checked if it has already been added to set. If so, skip to the next iteration. """
    if product in products:
        continue
    """ if not, the function checks whether the concatenated identity is pandigital. """
    if isPandigital(str(a) + str(b) + str(product)):
		    products.add(product)

print(sum(products))
