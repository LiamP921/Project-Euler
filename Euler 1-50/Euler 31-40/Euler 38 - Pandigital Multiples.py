""" calculates the largest 1-9 pandigital number formable via the concatenated product of an integer with '(1, 2, ... n)', where 'n > 1'. """
from itertools import product

def isPandigital(n, digits="123456789"):
    """ checks pandigitality of 'n' via string conversion, sorting, and comparison w/ 'digits', as per #32. """
    return "".join(sorted(str(n))) == digits

pandigital_products = []
""" generated cartesian products represent the concatenated products of the base integer and the maximum no. of integers. """
for a, n in product(range(1, 10000), range(2, 10)):
    """ formed via by the multiplication of 'a' by each integer in the range '(1, n)'. """
    concatinated_product = int("".join(str(a * i) for i in range(1, n + 1)))
    if len(str(concatinated_product)) != 9:
        continue
    if isPandigital(concatinated_product):
        pandigital_products.append(concatinated_product)

""" sort list in reverse and print the largest element if it isn't empty. """
pandigital_products.sort(reverse=True)
if pandigital_products:
    print(pandigital_products[0])
