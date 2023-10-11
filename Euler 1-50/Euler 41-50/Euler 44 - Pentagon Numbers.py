""" determines the pair of pentagonals(generated via 'Pn = n(3n − 1) / 2'), 'Pj and Pk', for which their sum and difference 
are pentagonal and 'D = |Pk − Pj|' is minimised; calculate 'D'. """
from math import sqrt

def findPentSumAndMinimisedDiff():
    P = lambda n: n * (3 * n - 1) // 2
    """ arbitrary limit of generated pentagonals. """
    pentagonals = set(P(n) for n in range(2200 + 1))
    p = 1  
    while True:     
        """ let 'D = p(3p - 1) / 2'. """
        D = P(p)
        """ iterate over all pentagonals 'k' <= to 'D'. """
        for k in pentagonals:
            if k <= D:
                continue
            """ for each 'k', calculate the difference 'j = k - D', and check if 'j' is also pentagonal. """
            j = k - D
            if j in pentagonals:
                S = k + j
                q = (1 + sqrt(1 + 24 * S)) / 6
                """ if 'q' is an integer, the pair 'Pj' and 'Pk' are found. """
                if q.is_integer():
                    return D
        p += 1

print(findPentSumAndMinimisedDiff())
