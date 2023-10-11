""" calculates the sum of all 0-9 pandigitals that satisfy the substring divisibility property (i.e. that every three adjacent 
digits form a number divisible by a specific prime). """

def hasUniqueDigits(digits):
    """ check for a 3-digit number w/ 3 unique digits. """
    if len(digits) != 3:
        return False
    return (digits[0] == digits[1]) or (digits[1] == digits[2]) or (digits[0] == digits[2])


def countPandigitalsStartingWith(sequence, index, total, valid_len, valid_sequences):
    """ recursively generate all pandigitals with the starting sequence of digits that satisfy the SDP."""
    if index == valid_len:
        total += int(sequence)
    else:
        pair = sequence[-2:]
        """ append the valid 3rd digit to the sequence and recursively call w/ the updated sequence and index until sequence's 
        length = valid_sequences's length. """
        if pair in valid_sequences[index]:
            for digit in valid_sequences[index][pair]:
                if digit not in sequence:
                    total = countPandigitalsStartingWith(sequence + digit, index + 1, total, valid_len, valid_sequences)
    return total

def createValidSequences(factors):
    """ create a list of dictionaries of valid sequences for each prime."""
    valid_sequences = []
    for i in range(len(factors)):
        current_map = {}
        """ for each prime, generate all valid triples that have unique digits. """
        for j in range(factors[i], 1000, factors[i]):
            """ '.zfill()' returns a copy of the string with 'n' 0s padded to the left. """
            digits = str(j).zfill(3)

            """ pruning numbers w/ non-unique digits, """
            if hasUniqueDigits(digits):
                continue

            """ creating a mapping between the first 2 digits and the 3rd digit for each number.  """
            if digits[:2] not in current_map:
                current_map[digits[:2]] = [digits[2]]
            else:
                current_map[digits[:2]].append(digits[2])

        valid_sequences.append(current_map)
    return valid_sequences

def main():
    factors = [1, 2, 3, 5, 7, 11, 13, 17]
    valid_sequences = createValidSequences(factors)
    valid_len = len(factors)
    total = 0

    """ count pandigitals starting w/ each valid pair of digits. """
    for pair in valid_sequences[0]:
        if pair[0] == "0":
            continue
        for digit in valid_sequences[0][pair]:
            triple = pair + digit
            total = countPandigitalsStartingWith(triple, 1, total, valid_len, valid_sequences)

    return total

print(main())
