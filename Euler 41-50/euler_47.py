"""
Distinct Primes Factors
--------------------------
The first two consecutive numbers to have two distinct prime factors are: 14 = 2 * 
7, 15 = 3 × 5

Find the smallest of the first n consecutive integers to have k distinct prime 
factors each. """

def distinct_primes_factors(limit, num_integers, num_factors):
    """ arbitrary limit of numbers to count the number of distinct prime factors 
    for. """
    factor_counts = [0] * limit
    sequence_count = 0
    for num in range(2, limit):
        """ if num has num_integers distinct prime factors. """
        if factor_counts[num] == num_integers:
            sequence_count += 1
            """ if num_factors consecutive numbers have been found with 
            num_integers distinct prime factors. """
            if sequence_count == num_factors:
                """ return the smallest. """
                return num - num_factors + 1
        else:
            """ reset sequence_count. """
            sequence_count = 0
            """ if num's number of distinct prime factors hasn't been checked 
            yet. """
            if factor_counts[num] == 0:
                """ num is prime, so mark its multiples with incremented factor 
                counts. """
                factor_counts[num :: num] = [count + 1 for count in factor_counts[num :: num]]

if __name__ == "__main__":
  print(distinct_primes_factors(150_000, 4, 4))
