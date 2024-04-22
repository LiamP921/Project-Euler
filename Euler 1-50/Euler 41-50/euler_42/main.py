"""
Coded Triangle Numbers
-------------------------------
The nth triangle numbers is given by: tn = 0.5(n(n + 1)). Converting each 
letter in a word to a number corresponding to its alphabetical position and adding 
these values yields a word value (e.g. SKY = 19 + 11 + 25 = 55 = t10). 

Calculate the number of words with triangular numbered values in the given text file.
"""

def _is_triangle(num):
    """ A number is triangular if 8(num) + 1 is odd and a perfect square. """
    n = 8 * num + 1
    if n % 2 == 0:
        return 0
    i = 3
    """ := assigns and returns a value in the same expression. """
    while (square := i * i) <= n:
        if square == n:
            return 1
        i += 2
    return 0

def coded_triangle_numbers():
    with open("words.txt", "r") as file:
        words = file.readline().strip().split(",")
    triangle_words = 0
    for word in words:
        word_value = sum(ord(char) - 64 for char in word.strip('"'))
        triangle_words += _is_triangle(word_value)
    return triangle_words

if __name__ == "__main__":
    print(coded_triangle_numbers())
