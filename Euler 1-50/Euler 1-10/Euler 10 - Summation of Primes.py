""" finds sum of primes below 'limit' """
def findPrimes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False
    """ 'enumerate' iterates over list, whilst tracking the index of the current element; returns an 'enumerate object', 
    an iterator that generates a tuple containing a count and the values obtained from iterating. """
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            """ 'yield' pauses function execution to return a 'generator object' (an iterator able to iterate over 
            a generated sequence of values) to the caller, storing local variable states to save memory overhead. """
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False

ans = findPrimes(2000000)
print(sum(ans))
