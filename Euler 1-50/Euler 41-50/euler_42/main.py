""" via a text file, sums each individual word's letter's alphabetical values, before summing the number of triangular 'word scores' (given by 'tn = 1/2n(n + 1)')."""
def getTriangularNumbers(max_value):
    """ return a set of triangular numbers up to max_value. """
    triangular_numbers = set()
    n = 1
    tn = 1
    while tn <= max_value:
        triangular_numbers.add(tn)
        n += 1
        tn = n * (n + 1) // 2
    return triangular_numbers

def main():
    """ evaluate the number of words whose value is a triangular number. """
    letter_number = {chr(i): i - 64 for i in range(65, 91)}
    """ max value for a 30-letter word. """
    triangular_numbers = getTriangularNumbers(26 * 30)
    
    with open("Words.txt") as file_object:
        words = file_object.readline()
        words_list = words.split(",")
        words_list = [word[1:-1] for word in words_list]
        
        triangular_count = 0
        for word in words_list:
            word_value = sum(letter_number[letter] for letter in word.upper())
            if word_value in triangular_numbers:
                triangular_count += 1
    
    print(triangular_count)

main()
