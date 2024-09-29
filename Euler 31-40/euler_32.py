""" Pandigital Products
--------------------
An n-digit number is pandigital if it uses all the digits 1-n exactly once. The product 
7254 is unusual, as the identity, 39 × 186 = 7254 is 1-9 pandigital.

Sum all the products whose multiplicand/multiplier/product identity is writable as a 
1 through n pandigital. """

def pandigital_products(n):
    products = set()
    digits = set("1234567890"[:n])
    for i in range(2, 80):
        j = i + 1
        """ product can never > four digits, so it must be < 9999. However, there 
        are no valid factors that could create a product with a first digit 9. """
        while i * j < 8999:
            """ if the concatenation of i, j, and i * j forms a pandigital of 
            length n. An empty resulting string means all digits 1-n were used 
            exactly once. """
            identity = "".join([str(i), str(j), str(i * j)])
            if len(identity) == n and set(identity) == digits: 
                products.add(i * j)
            j += 1
    """ set ensures each product is unique """
    return sum(products)

if __name__ == "__main__":
    print(pandigital_products(9))
