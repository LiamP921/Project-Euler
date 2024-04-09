import math

def largest_series_product(n):
    with open("number.txt", "r") as file:
        num = file.read().replace("\n", "")

    product = 0
    """ manage the n-size sliding window. """
    current_min, current_max = 0, n

    while current_max <= len(num):
        """ extract length n substring from num. """
        substring = num[current_min:current_max]
        """ math.prod() calculates the product of all the elements present in the given 
        iterable. """
        val = math.prod(int(sub) for sub in substring)
        if val > product:
            product = val
        current_min += 1
        current_max += 1
    """ when all substrings have been iterated through. """
    return product

if __name__ == "__main__":
    print(largest_series_product(13))
