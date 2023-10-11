""" calculates the sum of all amicable numbers < 'n' (two different numbers in which the sum of the proper divisors of each is equal to the other number). E.g. PDs of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220. """

def sumDivisors(n):
    """ returns the sum of all divisors of 'n'. """
    div_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        """ if 'n' is divisible by the current number, the divisor is summed. """
        if n % i == 0:
            div_sum += i
            """ if the divisor != to sqrt('n'), the quotient obtained by dividing 'n' by the divisor is summed. """
            if i != n // i:
                div_sum += n // i
    return div_sum

def amicableNumbers(n):
    """ returns the sum of all amicable numbers < 'n'. """
    amicable_sum = 0
    for i in range(1, n):
        """ for each 'i', calculate the sum of its proper divisors; then, calculate the sum of proper divisors of 'div_sum_i'. """
        div_sum_i = sumDivisors(i)
        div_sum_j = sumDivisors(div_sum_i)
        """ if the value of 'div_sum_j' = 'i', and 'i' != 'div_sum_i', 'i' is amicable. """
        if div_sum_j == i and i != div_sum_i:
            amicable_sum += i

    return amicable_sum

print(amicableNumbers(10000))
