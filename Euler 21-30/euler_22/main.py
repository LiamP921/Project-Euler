"""
Names Scores
--------------
Alphabetise a file names.txt. Then, work out the alphabetical value for each name, and multiply this by the name's position 
to obtain a score.
Calculate the total of all the name scores in the array.
"""

def name_score():
    with open("names.txt", "r") as file:
        names = file.readline().strip().split(",")
    sorted_names = _quick_sort(names, 0, len(names) - 1) # see Netronomicon/__pycache__/helper/quick_sort.py
    total_score = 0
    """ for each name, calculate its alphabetical value by summing the ASCII values of 
    its characters and subtracting 64; enumerate() returns an iterator with index and 
    element pairs from an iterable. ord() returns the unicode value of a character. """
    for index, name in enumerate(sorted_names):
        name_value = sum(ord(char) - 64 for char in name.strip('"'))
        """ multiply value by index for name score. """
        total_score += (index + 1) * name_value
    return total_score

if __name__ == "__main__":
    print(name_score())
