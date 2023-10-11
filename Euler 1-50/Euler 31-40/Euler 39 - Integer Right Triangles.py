""" considering 'p' as the perimeter of a RAT with integral side lengths {a,b,c}, calculates the value 'p <= n' in which the no. of solutions is maximised. """
from collections import defaultdict

def maxPythagoreanTriplet(p_limit):
    """ 'defaultdict' is a dictionary sub-class which never raises a 'KeyError', instead providing a default value for yet unseen keys. """
    perimeters_dict = defaultdict(set)
    for k in range(1, p_limit // 2):
        m = 1
        p = 0
        while p <= p_limit:
            m += 1
            for n in range(1, m):
                """ PT formula, rearranged from #9. """
                a = (km2 := k * m * m) - (kn2 := k * n * n)
                b = k * 2 * m * n
                c = km2 + kn2
                """ if triplet sum (perimeter) is '<= p_limit', add triplet to the set corresponding to key 'p' (where 'p' is the perimeter) """
                if (p := a + b + c) <= p_limit:
                    perimeters_dict[p].add(tuple(sorted([a,b,c])))
    """ '.keys()' returns a view object displaying a list of all dictionary keys in insertion order; 'lambda' functions take any number of arguments, but have only one expression. """
    return max(perimeters_dict.keys(), key = lambda k: len(perimeters_dict[k]))

""" when all 'k' values are considered, the above key function returns the length of the set of PTs for each key 'k'. """
print(maxPythagoreanTriplet(1000))
