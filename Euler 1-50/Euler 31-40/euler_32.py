"""
Pandigital Products
--------------------
An n-digit number is pandigital if it uses all the digits 1-n exactly once. The product 
7254 is unusual, as the identity, 39 × 186 = 7254 is 1-9 pandigital.

Sum all the products whose multiplicand/multiplier/product identity is writable as a 
1 through n pandigital.
"""

def pandigital_products(n):
    digits = set(map(str, range(1, n + 1)))
    products = set()
    """ maximum possible multiplicand ensures the product remains within a 4-digit 
    number. """
    for i in range(2, 80):
        for j in range(2, 9000 // i):
            """ if the concatenation of i, j, and i * j forms a pandigital of 
            length n. An empty resulting string means all digits from 1-n were used 
            exactly once. """
            product = i * j
            identity = "".join([str(i), str(j), str(product)])
            if len(identity) == n and set(identity) == digits:
                """ set ensures that each product is unique. """
                products.add(product)
    return sum(products)

if __name__ == "__main__":
    print(pandigital_products(9))
