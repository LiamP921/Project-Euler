"""
Pandigital Products
--------------------
An n-digit number is pandigital if it uses all the digits 1-n exactly once. The product 
7254 is unusual, as the identity, 39 × 186 = 7254 is 1-9 pandigital.

Sum all the products whose multiplicand/multiplier/product identity is writable as a 
1 through n pandigital.
"""

def pandigital_products(n):
    products = set()
    """ maximum possible multiplicand to ensure the product remains within a 4-digit number. """
    for i in range(2, 80):
        for j in range(1, 9876 // i):
            """ if the concatenation of i, j, and i * j forms a pandigital of 
            length n. An empty resulting string means all digits from 1-n were used 
            exactly once. """
            if len(str(i) + str(j) + str(i * j)) == n and not "123456789"[:n].strip(str(i) + str(j) + str(i * j)):
                """ set ensures that each product is unique. """
                products.add(i * j)
    return sum(products)

if __name__ == "__main__":
    print(pandigital_products(9))
