"""
Large Sum
-----------
Work out the first n digits of the sum of the given numbers.
"""

def large_sum(n):
    """ Because only one digit is truncated every time a carry value is added to the list, 
    there will never be more entries than the maximum number of digits in the carry value. 
    For instance, if there's a 9 in each carry value, the sum will be log(n * 9) * 9. """ 
    with open("numbers.txt", "r") as file:
        numbers = []
        for line in file:
            numbers.append(line.strip())
  
    result = ''
    """ while there are numbers left in the string, accummulate a sum of the LSD. """
    while len(numbers) > 0:
        sum_of_digit_position = 0
        for number_string in numbers:
            sum_of_digit_position += int(number_string[-1])
        """ LSD of this sum is the new MSD in the result. """
        result = str(sum_of_digit_position)[-1] + result
  
        i = 0
        while i < len(numbers):
            """ if the string has 1/0 digits, remove it from the list as it won't 
            contribute to the sum. """
            if len(numbers[i]) <= 1:
                del numbers[i]
            else:
                """ since all the LSDs for each number have already been summed, 
                and recorded that digit's value in the result, they're no longer 
                needed. """
                numbers[i] = numbers[i][:-1]
                i += 1
  
        if sum_of_digit_position > 9:
            """ if the sum of all LSDs > 9, add the carry value (the sum less its LSD) 
           as a number to be summed. """
            numbers.append(str(sum_of_digit_position)[:-1])
    return result[:n]

if __name__ == "__main__":
    print(large_sum(10))
