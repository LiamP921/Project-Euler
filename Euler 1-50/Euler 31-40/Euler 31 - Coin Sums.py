""" calculates the no. of distinct permutations, using any number of British coins, that equate to '£n'. """
def coinPermutations(n):
    """ coin denominations in pence. """
    coins = [1, 2, 5, 10, 20, 50, 100, 200] 
    """ pounds to pence. """
    n = int(n * 100)
    permutations = [0] * (n + 1)
    """ only one permutation to make 0p. """
    permutations[0] = 1

    for coin in coins:
        for amount in range(coin, n+1):
            permutations[amount] += permutations[amount - coin]

    return permutations[n]

print(coinPermutations(2))
