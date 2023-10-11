""" calculates the 'nth' lexicographic permutation of the digits 0-9. """
def digitPermutation(n, digits):
    s = []
    result = ""
    digits = list(digits)
    """ as per the factoradic method, decrement 'n' by 1, as the sorted order is considered the '0th' permutation. """
    n -= 1

    for i in range (1, len(digits) + 1):
        """ iteratively divide 'n' by 'digits' length, storing the remainder in a stack each time. """
        s.append(n % i)
        """ update value of 'n'. """
        n //= i
      
    for i in range(len(digits)):
        a = s[-1]
        """ once the stack is populated, append the last list element to result. """
        result += digits[a]
        for j in range(a, len(digits) - 1):
            digits[j] = digits[j + 1]
        """ remove the selected digit from 'digits', effectively reducing available digits for the next selection. """
        digits[j + 1] = "\0"
        """ last list element is popped, repeating the process for all remaining digits. """
        s.pop()

    print(result)

digitPermutation(1000000, "0123456789")
