""" finds sum of even Fibonacci numbers below 'n' """
def evenFibonacciNumbers(n):
    f1, f2 = 1, 2
    s = 0
    while f2 <= n:
        if f2 % 2 == 0:
            s += f2
        f1, f2 = f2, f1+f2
        print(s)   

fibonacciNumbers(4000000)
