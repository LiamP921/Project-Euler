""" Smallest Multiple
-----------------------
2520 is the smallest number that can be divided by each of the numbers 1 to 10 
without any remainder.
Find the smallest positive number that's evenly divisible by all the numbers 1 to n. """

def _greatest_common_divisor(a, b):
    while b:
        """ Euclidean algorithm repeatedly applies the property that the GCD of two 
        numbers is the same as that of one of the numbers and the remainder of 
        dividing the other number by the first. """
        a, b = b, a % b
    return a

def _lowest_common_multiple(a, b):
    """ the product of two numbers is equal to the product of 
    their GCD and LCM. """
    return (a * b) // _greatest_common_divisor(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(2, n + 1):
        result = _lowest_common_multiple(result, i)
    return result

if __name__ == "__main__":
    print(smallest_multiple(20))
