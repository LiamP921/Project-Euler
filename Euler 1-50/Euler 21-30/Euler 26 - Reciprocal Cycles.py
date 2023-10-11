""" calculates the value of 'd < n' for which '1/d' contains the longest recurring decimal cycle. """
def recurringDecimalCycle(n):
    remainder = 1
    cached_remainders = {}
    i = 0
    while remainder != 0 and remainder not in cached_remainders:
        cached_remainders[remainder] = i
        """ when performing the long division '1 / n', the remainder at each step will repeat after a certain number of steps if the division isn't exact, giving the length of the RDC. """
        remainder = (remainder * 10) % n
        i += 1
    if remainder == 0:
        """ has no RDC. """
        return 0
    else:
        """ difference between current index and index of the first occurrence of the remainder in the dictionary. """
        return i - cached_remainders[remainder]

def longestRecurringDC(n):
    max_rdc_length = 0
    max_number = 0
    for d in range(1, n):
        length = recurringDecimalCycle(d)
        if length > max_rdc_length:
            max_rdc_length = length
            max_number = d
    return max_number

print(longestRecurringDC(1000))
