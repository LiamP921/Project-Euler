"""
Longest Collatz Sequence
-------------------------
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using this rule above and starting with 13, the following sequence is generated:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting and finishing at 13 and 1) contains 10 terms. 
It's thought that all starting numbers finish at 1.
Find which starting number, under the given limit, produces the longest chain.
Note: Once the chain starts, the terms are allowed to exceed the limit.
"""

def _count_chain(n):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        """ 1a). If n is even, n → n // 2 ⇒ Collatz(n) = Collatz(n // 2) + 1. 
        Therefore, Collatz(2k) > Collatz(k) for all k. """
        memo[n] = 1 + _count_chain(n // 2)
    else:
        """ 2). If n is odd, 3n + 1 is even, and n → 3n + 1 → (3n + 1) // 2. 
        A step can be saved by giving Collatz(n) = Collatz((3n + 1) // 2) + 2. """
        memo[n] = 2 + _count_chain((3 * n + 1) // 2)
    return memo[n]

def longest_collatz_sequence(n):
    longest_chain = 0
    answer = -1

    """ 1b). Therefore, there's no need to compute the chain for any k ≤ LIMIT // 2. """
    for number in range(n // 2, n):
        chain_length = _count_chain(number)
        if chain_length > longest_chain:
            longest_chain = chain_length
            answer = number
    return answer

if __name__ == "__main__":
    memo = {1: 1}
    print(longest_collatz_sequence(1_000_000))
