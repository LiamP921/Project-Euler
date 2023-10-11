""" calculate the last 'n' digits of the value of the series '1^1 + 2^2 + 3^3 + ... + n^n'. """
def sumOfSelfPowers(n):
    """ represents the modulo value of '10^10'. """
    mod = 10 ** 10
    result = 0
    for i in range(1, n + 1):
        """ 'i' raised to the power of 'i' modulo 'mod'. """
        result += pow(i, i, mod)
    return str(result % mod)

print(sumOfSelfPowers(1000)[-10:])
