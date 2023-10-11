""" sorts a text file into alphabetical order, before summing individual products of the sum of each letter's alphabetical value and the name's list position. """
def nameSum(name):
    """ get count of a single name via ASCII codes. """
    letter_number = {chr(i):i - 64 for i in range(65, 91)}
    total = 0
    for letter in name.upper():
        total += letter_number[letter]
    return total

def sortNames():
    """ import text file and add names to a list, before sorting it. """
    with open("Names.txt") as file_object:
        names = file_object.readline()
        names_list = names.split(",")
        names_list = [name[1:-1] for name in names_list]
        names_list.sort()
        return names_list

def main():
    """ evaluate totals of all scores in text file. """
    name_list = sortNames()
    length = len(name_list)
    total = 0
    for i in range(1, length + 1):
        total += i * nameSum(name_list[i - 1])
    print(total)

main()
