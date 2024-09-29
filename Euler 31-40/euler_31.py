""" Coin Sums
-----------------
There are eight coins in general circulation in UK currency: 1p, 2p, 5p, 10p, 20p, 50p, 
£1 (100p), and £2 (200p). £2 can be made as such: 1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 
3*1p.
Calculate how many different ways n pence can be made using any number of coins. """

def coin_sums(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    """ for each coin, update the number of ways to make each amount, considering the 
    current denomination. """
    for coin in coins:
        for j in range(coin, n + 1):
            """ add the number of ways to make j pence using the current denomination 
            to that of making (j - coin) pence. This constructs the number of ways to 
            make each amount using the available denominations. """
            ways[j] += ways[j - coin]
  
    return ways[n]

if __name__ == "__main__":
    print(coin_sums(200))
