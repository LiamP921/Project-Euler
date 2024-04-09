"""
Number Letter Counts
------------------------
If the numbers 1 to 5 are written out: one, two, three, four, five, there are 3 + 3 + 5 
+ 4 + 4 = 19 total letters used.
Calculate how many letters would be used if all the numbers from 1 to limit inclusive 
were written out.
Notes: Don't count spaces or hyphens (e.g. three hundred and forty-two and one hundred 
and fifteen contain 23 and 20 letters). The use of "and" when writing out numbers is in 
compliance with British usage.
"""

def number_letters_count(n):
    def count_letters(num):
        if num < 10:
            """ return the lengths of the corresponding words from the lists. """
            return len(["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][num])
        elif num < 20:
            return len(["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][num - 10])
        elif num < 100:
            """ calculate the length of the word representing the tens place and add 
            it to the word length representing the ones place (if any). """
            return len(["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][num // 10 - 2]) + count_letters(num % 10)
        elif num < 1000:
            """ calculate the length of the word representing the hundreds place, 
            add the length of "hundred", and if there are any remaining digits, add 
            the length of "and" followed by the count of letters for the remaining 
            number. """
            return count_letters(num // 100) + len("hundred") + (0 if num % 100 == 0 else len("and") + count_letters(num % 100))
        else:
            return len("onethousand")
  
    total_letters = 0
    for i in range(1, n + 1):
        total_letters += count_letters(i)
    return total_letters

if __name__ == "__main__":
  print(number_letters_count(1000))
