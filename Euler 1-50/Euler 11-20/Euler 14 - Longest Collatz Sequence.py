""" calculates which starting number, below 'n', produces the longest Collatz sequence """
cache = {}

def collatzSequence(n):
    if not n in cache:
        if n == 1:
            """ 'memoisation' optimises rercursion by caching already computed results, returning it when inputs reoccur. """
            cache[n] = 1
        elif n % 2 == 0:
            cache[n] = collatzSequence(n // 2) + 1
        else:
            cache[n] = collatzSequence(3 * n + 1) + 1
    return cache[n]

def longestCS(n):
    max_length = 0
    max_number = 0
    for i in range(1, n):
        length = collatzSequence(i)
        if length > max_length:
            max_length = length
            max_number = i
    return max_number

print(longestCS(1000000))
