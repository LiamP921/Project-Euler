""" calculates greatest product of thirteen adjacent digits """
def product(s, j):
    p = 1
    for i in range(j, j + 13):
        p *= s[i]
    return p

with open("1000-Digits.txt") as file_object:
    """ 'strip' removes trailing whitespace; 's' converts string into a list of integers """
    s = [int(c) for line in file_object for c in line.strip()] 

n = len(s)
maxProduct = 0

for j in range(n - 12):
    c = product(s, j)
    if c > maxProduct:
        maxProduct = c

print(maxProduct)
