""" calculates the first 'n' digits of the sum of 'm' 'k'-digit numbers. """
def firstNDigitsOfSum(n):
    with open("One-Hundred 50-Digits.txt") as file_object:
        numbers = [int(line.strip()) for line in file_object]
    total = str(sum(numbers))
    return int(total[:n])

print(nDigitsOfNSum(10))
