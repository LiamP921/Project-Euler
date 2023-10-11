""" finds largest palindrome constructable via two 3-digit numbers. """ 
def palindromicProducts(n):
    return str(n) == str(n)[::-1]

arr = []

for i in range(100, 1000):
    for j in range(100, 1000):
        elem = i * j
        if palindromicProducts(elem):
            arr.append(elem)
            
print(max(arr))
