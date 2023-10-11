""" calculates the number of letters used to write out every number from 1 to 'n', inclusive; doesn't count spaces or hyphens. """
def countLetters(n):
    digit_words = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teen_words = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    ten_words = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    def convertTens(num):
        """ look up the number's corresponding strings in the respective dictionaries. """
        if num < 10:
            return digit_words[num]
        elif num < 20:
            return teen_words[num]
        else:
            """ if not 10-19, split number into tens and units before utilising the respective dictionaries. """
            ten_word = ten_words[num // 10]
            if num % 10 == 0:
                return ten_word
            else:
                """ concatenate the tens and units strings.  """
                return ten_word + "-" + digit_words[num % 10]
  
    def convertHundreds(num):
        """ splits a number from 100-999 into hundreds, tens and units. """
        hundred_word = digit_words[num // 100] + " hundred"
        if num % 100 == 0:
            return hundred_word
        else:
            """ concatenate the hundreds string w/ remaining digits string. """
            return hundred_word + " and " + convertTens(num % 100)

    def convertNumber(num):
        if num < 10:
            return digit_words[num]
        elif num < 100:
            return convertTens(num)
        elif num < 1000:
            if num % 100 == 0:
                return digit_words[num // 100] + " hundred"
            else:
                return convertHundreds(num)
        else:
            return "one thousand"

    total_letters = 0
    for i in range(1, n + 1):
        """ converts each number into string rep., removes all spaces and hyphens, and adds the resulting strings' lengths. """
        num_word = convertNumber(i)
        num_letters = len(num_word.replace(" ", "").replace("-", ""))
        total_letters += num_letters
    return total_letters

print(countLetters(1000))
