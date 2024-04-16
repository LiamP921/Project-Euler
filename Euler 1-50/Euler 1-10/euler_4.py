"""
Largest Palindrome Product
---------------------------
Palindromic numbers read the same both ways; the largest obtainable from the product 
of two 2-digit numbers is 9009 = 91 * 99. 
Find the largest palindrome made from the product of two n-digit numbers.
"""

def _is_palindrome(n):
    k = n
    reversed = 0
    """ iteratively take the last digit of the original number, 
    add it to reversed, after shifting the digits to the left,
    and remove the last digit from the original number. """
    while k > 0:
        reversed = 10 * reversed + k % 10
        k //= 10
    return n == reversed

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
  found_palindrome = False
  done = False

  while not done:
      """
      iterate downwards from the largest possible factor.
      """
      max_first_factor = 10 ** n_digits - 1
      max_first_factor_mod_11 = (max_first_factor - 11) // 22 * 22 + 11
      min_second_factor = 10 ** n_digits - 10 ** (n_digits - first_factor_digits) + 1
      if 2 * first_factor_digits == n_digits:
          largest_palindrome = max_first_factor * min_second_factor
      else:
          largest_palindrome = min_second_factor * min_second_factor
      """
      step size of 22 and modulo 11 ensures x is relatively prime to 10, 
      which is necessary to apply Hensel's lemma.
      """
      modulo = 10 ** first_factor_digits

      x = max_first_factor_mod_11
      while x > 1 and not found_palindrome:
          if x * max_first_factor < largest_palindrome:
              found_palindrome = True
          else:
              """
              if p is a palindrome modulo m, the modular_inverse also is. This 
              optimises the search for factor pairs, as it allows one factor to be 
              found by reversing the digits another factor modulo some modulus, 
              removing the need to consider all possible pairs.
              """
              reverse_second_factor = _modular_inverse(x, modulo)
              if reverse_second_factor is not None:
                  max_second_factor = max_first_factor + 1 - reverse_second_factor
                  p = max_second_factor * x

                  while p > largest_palindrome:
                      if _is_palindrome(p) and p > largest_palindrome:
                          largest_palindrome = p
                      p -= x * modulo
          x -= 22
      done = True
  return largest_palindrome

if __name__ == "__main__":
    print(largest_palindrome(3))
