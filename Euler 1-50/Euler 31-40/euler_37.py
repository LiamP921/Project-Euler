"""
Truncatable Primes
--------------------
3797 remains prime at each stage of having its digits continuously removed from 
left to right and vice versa.
Sum all the primes which are truncatable from left to right and vice versa.
"""

def _is_left_truncatable(n):
    """ smallest digit position. """
    mod = 10
    """ check if all truncated numbers are prime. """
    while mod < n:
        if not _miller_rabin(n % mod): # see Python-Recreational-Mathematics/primality/miller_rabin.py
            return False
        """ iterate through digits from right to left by increasing mod by a 
        factor of 10. """
        mod *= 10
    return True

def truncatable_primes():
    """ truncatable primes can only start with: """
    primes = [2, 3, 5, 7]
    """ thus, the remaining digits have to be: """
    push_arr = [1, 3, 7, 9]
    push_size = 4
    total_sum = 0

    """ while there are elements in primes, pop the first to ensure that 
    candidates are already right-truncatable. """
    while primes:
        current_prime = primes.pop(0)
        """ append each digit to this prime to create new numbers that are checked 
        for primality."""
        for i in range(push_size):
            new_number = current_prime * 10 + push_arr[i]
            if _miller_rabin(new_number):
                primes.append(new_number)
                if _is_left_truncatable(new_number):
                    total_sum += new_number
  
    return total_sum

if __name__ == "__main__":
    print(truncatable_primes())
