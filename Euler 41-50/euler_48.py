""" Self Powers
---------------------
11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series: 1^1 + 2^2 + 3^3 + ... + n^n. """

""" 1). Knowing how a sum and product behave under a modular congruence relation (i.e. 
when they have equivalent post-modular remainders) solves the problem quickly: 
n∑i=1 i^i ≡ n∑i=1 (i^i mod m) (mod m).

2). Now that i^i mod m has been isolated, it can be solved under the following: 
i^i ≡ i∏j=1 i ≡ i∏j=1 i (i mod m) (mod m).

3). The inner loop is further optimised via exponeniation by squaring, by 
stating the products recursively so that: 
x^y (mod p) ≡ (x mod p), if y = 1.
(x^2 mod p)^((y - 1) / 2), if y is odd.
(x^2 mod p)^(y / 2), if y is even. """

def self_powers(n, m):
    s = 0
    for i in range(1, n + 1):
        """ Each term can be constrained to <= 10 digits, fitting into one 64-
        bit word. They're then aggregated and reduced at each step to ensure that 
        they all remain bounded by 10^10. """
        s += _modular_exponent(i, i, m) # see Recreational-Algorithms/number_theory/miller_rabins.py
        s %= m
    return s

if __name__ == "__main__":
    print(self_powers(1000, 10 ** 10))
