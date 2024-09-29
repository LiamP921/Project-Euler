""" Digit Fifth Powers
-----------------------------
Only three numbers can be written as the sum of fourth powers of their digits: 1634 (14 
+ 64 + 34 + 44), 8208 (84 + 24 + 04 + 84), and 9474 (94 + 44 + 74 + 44).
Sum all the numbers writable as the sum of n powers of their digits. """

""" Each complete permutation of six digits has the same power sum. Thus, time can be saved 
by calculating the power sum of each digit set, and recording the digit power sums which 
exactly match the set. """

import math

def _generate_groups(num_digits, lower=0, upper=9):
    """ generate unique combinations of digits of a certain length by building 
    groups."""
    if num_digits == 1:
        for digit in range(lower, upper + 1):
            yield [digit]
    else:
        for digit in range(lower, upper + 1):
            for sub_group in _generate_groups(num_digits - 1, digit, upper):
                group = [digit]
                group.extend(sub_group)
                yield group

def digit_n_powers(n):
    num_digits = 0 
    reached_limit = False

    """ calculate the maximum number of digits by iterating until a limit, where 
    adding one more digit would not increase the maximum possible number, is found. """
    while not reached_limit:
        if math.log10((num_digits + 1) * (9 ** n)) + 1 < (num_digits + 1):
            reached_limit = True
        else:
            num_digits += 1 

    """ smallest digit such that the number formed by repeating this digit num_digits 
    times raised to the power of n > the maximum possible number. """
    limit_digit = min([int(digit) for digit in str(num_digits * 9 ** n)])
    number_list = set()

    """ check if the first digit of each group exceeds the limit digit. If not, check 
    if the sum of the nth powers of the digits in the group equals a number composed 
    entirely of those digits. If so, add that number to the result set. """
    for group in _generate_groups(num_digits):
        if group[0] > limit_digit:
            reached_limit = True  
        else:
            all_digits_valid = True
            exp_sum = str(sum([digit ** n for digit in group]))

            for digit in exp_sum:
                digit_num = int(digit)
                if digit_num in group:
                    group.remove(digit_num)
                else:
                    all_digits_valid = False
            if all_digits_valid and sum(group) == 0:
                number_list.add(int(exp_sum))

    number_list.remove(1)
    number_list.remove(0)
    return sum(number_list)

if __name__ == "__main__":
    print(digit_n_powers(5))
