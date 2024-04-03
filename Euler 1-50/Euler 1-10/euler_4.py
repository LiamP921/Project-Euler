"""
Largest Palindrome Product
---------------------------
Palindromic numbers read the same both ways; the largest obtainable from the product 
of two 2-digit numbers is 9009 = 91 * 99. 
Find the largest palindrome made from the product of two n-digit numbers.
"""

def _is_palindrome(x):
    """
    if x is divisible by 10 (i.e. if its last digit is 0) and it's != 0, 
    it can't be a palindrome because these can't start with 0.
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    """
    first and reversed second part of number.
    """
    head, tail = x, 0
    """
    ensures that only half of the digits are processed, as the entire number isn't
    needed to determine if it's palindromic.
    """
    while head > tail:
        """
        integer divide head by 10 to remove its last digit. the remainder of head 
        divided by 10 is then added to tail after being multiplied by 10, 
        effectively building the reversed first half of the number in tail.
        """
        head, tail = head // 10, tail * 10 + head % 10
    """
    If x has an odd number of digits, head will be one shorter than tail. Here, head
    needs to equal tail with the last digit removed to be palindromic. If the number 
    of digits in x is even, head and tail should be equal for the number to be 
    palindromic.
    """
    return head == tail or head == tail // 10

def _modular_inverse(x, modulus_power_of_10):
    """
    describes the integer product ax which is congruent to 1 with respect to the modulus m.(i.e. ax ≡ 1 (mod m))
    """
    inverse_table = [None, 1, None, 7, None, None, None, 3, None, 9]
    inverse = inverse_table[x % 10]
    if inverse is None:
        return inverse
    while True:
        """
        Hensel's lemma: if a univariate polynomial has a simple root modulo a prime
        p, this root can be lifted to a unique root modulo of any higher power of p.
        Here, the guess for the modular inverse is iteratively refined by computing
        ax mod modulus_power_of_10, where a is the number whose modular inverse is 
        sought, and x is the current guess.
        """
        ax = inverse * x % modulus_power_of_10
        if ax == 1:
            return inverse
        """
        If ax is 1, x is the modular inverse. Otherwise, update the guess via a 
        variation of Hensel lifting, which corrects the guess to ensure each 
        iteration approaches the actual modular inverse.
        """
        inverse = (inverse * (2 - ax)) % modulus_power_of_10

def largest_palindrome(n_digits):
    first_factor_digits = n_digits // 2

    while True:
        """
        iterate downwards from the largest possible factor.
        """
        max_first_factor = 10 ** n_digits - 1
        max_first_factor_mod_11 = (max_first_factor - 11) // 22 * 22 + 11
        min_second_factor = 10 ** n_digits - 10 ** (n_digits - first_factor_digits) + 1
        if 2 * first_factor_digits == n_digits:
            largest_palindrome = max_first_factor * min_second_factor
            factors = (max_first_factor, min_second_factor)
            assert _is_palindrome(largest_palindrome)
        else:
            largest_palindrome = min_second_factor * min_second_factor
            factors = None
        modulo = 10 ** first_factor_digits
        """
        step size and modulo 11 ensures x is relatively prime to 10, 
        which is necessary to apply Hensel's lemma.
        """
        for x in range(max_first_factor_mod_11, 1, -22):
            if x * max_first_factor < largest_palindrome:
                break
            """
            if p is a palindrome modulo m, the modular_inverse also is. This 
            optimises the search for factor pairs, as it allows one factor to be 
            found by reversing the digits another factor modulo some modulus, 
            removing the need to consider all possible pairs.
            """
            reverse_second_factor = _modular_inverse(x, modulo)
            if reverse_second_factor is None:
                continue
            max_second_factor = max_first_factor + 1 - reverse_second_factor
            """
            iterate through possible palindrome candidates from max_second_factor * 
            x, decrementing by x * modulo until it reaches the current largest 
            palindrome. if the current candidate is a palindrome > than the current 
            largest palindrome, update the largest palindrome and factors.
            """
            for p in range(max_second_factor * x, largest_palindrome, -x * modulo):
                if _is_palindrome(p) and p > largest_palindrome:
                    largest_palindrome = p
                    second_factor = p // x
                    factors = (x, second_factor)
                  
        if factors:
            return largest_palindrome, factors
        else:
            first_factor_digits -= 1

print(largest_palindrome(3))
