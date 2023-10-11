""" calculates which prime, < 'limit', can be written as the sum of the most consecutive primes. """
def sieve(limit):
    primes = [2, 3]
    is_prime = [True] * (limit - 1)
    """ iterate over every sixth odd from 5 and check primality. If it's prime, append to and mark all multiples 
    (excluding evens) as composite in 'is_prime'. Repeat for every sixth number that is two more than a multiple of six.  """
    for i in range(5, limit, 6):
        if is_prime[(i - 2) // 2]:
            primes.append(i)
            for j in range(i * i, limit, 2 * i):
                is_prime[(j - 2) // 2] = False
        if i + 2 < limit and is_prime[(i + 2 - 2) // 2]:
            primes.append(i + 2)
            for j in range((i + 2) * (i + 2), limit, 2 * (i + 2)):
                is_prime[(j - 2) // 2] = False
    return primes

def largestConsPrimeSequence(limit):
    prime_list = sieve(limit)
    prime_set = set(prime_list)
    longest_sum = 0
    longest_length = 0
    current_sum = 0
    i = 0
    j = 0
    """ inner loop repeatedly adds primes to 'current_sum' until the sum exceeds the limit, or until all primes have been added. 
    At each iteration, 'j' is incremented to add the next prime, and the length of the current sequence of primes ('length') 
    is computed as the difference between 'j and i'. """
    while j < len(prime_list):
        while j < len(prime_list) and current_sum + prime_list[j] <= limit:
            current_sum += prime_list[j]
            j += 1
        length = j - i
        """ if the length of the current sequence > 'longest_length', and the sum of the sequence ('current_sum') is prime 
        (checked via 'prime_set'), 'longest_sum' and 'longest_length' are updated. """
        if length > longest_length and current_sum in prime_set:
            longest_sum = current_sum
            longest_length = length
        current_sum -= prime_list[i]
        i += 1
    return longest_sum

print(largestConsPrimeSequence(1000000))
