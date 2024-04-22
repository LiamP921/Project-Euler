"""
Sub-String Divisibility
------------------------
With 1406357289, let d1 and d2 be the 1st and 2nd digit, and so on. In this way, we 
note the following: d2d3d4 = 406 is divisible by 2, d3d4d5 = 063 by 3, d4d5d6 = 635 
by 5, d5d6d7 = 357 by 7, d6d7d8=572 by 11, d7d8d9 = 728 by 13, d8d9d10 = 289 by 17

Sum all the 0-n pandigitals with sub-strings with this property.
"""

def has_unique_digits(sequence):
    return len(set(sequence)) < len(sequence)

def count_pandigitals(sequence, index, total, valid_len, valid_sequences):
    """ recursively generate all pandigitals with the starting sequence of digits 
    that satisfy the SDP."""
    if index == valid_len:
        total += int(sequence)
    else:
        pair = sequence[-2:]
        """ append the valid 3rd digit to the sequence and recursively call w/ the 
        updated sequence and index until sequence's length = valid_sequences's 
        length. """
        if pair in valid_sequences[index]:
            for digit in valid_sequences[index][pair]:
                if digit not in sequence:
                    total = count_pandigitals(sequence + digit, index + 1, total, valid_len, valid_sequences)
    return total

def create_valid_sequences(factors):
    """ list of dictionaries of valid sequences for each prime."""
    valid_sequences = []
    for i in range(len(factors)):
        current_map = {}
        """ for each prime, generate all valid triples that have unique digits. """
        for j in range(factors[i], 1000, factors[i]):
            """ .zfill() returns a copy of the string with 'n' 0s padded to the 
            left. """
            digits = str(j).zfill(3)

            """ prune numbers with non-unique digits, """
            if not has_unique_digits(digits):
                """ mapping between the first 2 and 3rd digits for each number.  """
                if digits[:2] not in current_map:
                    current_map[digits[:2]] = [digits[2]]
                else:
                    current_map[digits[:2]].append(digits[2])

        valid_sequences.append(current_map)
    return valid_sequences

def substring_divisibility():
    factors = [1, 2, 3, 5, 7, 11, 13, 17]
    valid_sequences = create_valid_sequences(factors)
    valid_len = len(factors)
    total = 0

    """ count pandigitals starting with each valid digit pair. """
    for pair in valid_sequences[0]:
      if pair[0] != "0":
          for digit in valid_sequences[0][pair]:
              triple = pair + digit
              total = count_pandigitals(triple, 1, total, valid_len, valid_sequences)
    return total

if __name__ == "__main__":
    print(substring_divisibility())
