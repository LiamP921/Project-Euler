""" calculates the first trianglular number w/ > 'n' divisors. """
def sieveOfEratosthenes(n):
    m = 150000
    primes = [True] * m
    p = 2
    count = 0

    while count < n:
        if primes[p]:
            count += 1
            for i in range(p * p, m, p):
                primes[i] = False
        p += 1

    primes_list = [i for i in range(2, m) if primes[i]]
    primes_list.sort()
    return primes_list

#--------------------------------------------------

def triangularNumber(n):
    """ generates primes up to 'n', as per #7. """
    primes_list = sieveOfEratosthenes(n)
    factors_count = 1
    i = 1
    while factors_count <= n:
        """ TN formula = 'x * (x + 1) / 2'; 'k' and 'k + 1' are co-primes, with two co-primes having a distinct prime factor set. """
        i += 1
        if i % 2 == 0:
            num1 = i // 2
            num2 = i + 1
        else:
            """ cases when 'x' is even and odd: 'x / 2' and '(x + 1)', and 'x' and '(x + 1) / 2' respectively, considered as two numbers whose prime factorisation is to be found. """
            num1 = i
            num2 = (i + 1) // 2
        triangular_number = num1 * num2
        factors_count = 1
        j = 0

        """ PF found by iterating through 'primes_list' and counting the no. of times each prime divides the TN. """
        while triangular_number > 1 and primes_list[j] * primes_list[j] <= triangular_number:
            exponent = 0
            while triangular_number % primes_list[j] == 0:
                exponent += 1
                triangular_number //= primes_list[j]
            factors_count *= exponent + 1
            j += 1

        """ if TN has doesn't have > 'n' divisors, increment 'i' to find the next. """
        if triangular_number > 1:
            factors_count *= 2
    return num1 * num2

print(triangularNumber(500))
