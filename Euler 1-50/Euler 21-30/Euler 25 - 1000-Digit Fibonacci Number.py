""" calculates index of the first 'n'-digit Fibonacci number. """
def nthDigitFibonacci(num_digits):
    fib = [0, 1]
    index = 1
    while len(str(fib[-1])) < num_digits:
        """ calculates Fibonacci Sequence via index of two most-recently added terms. """
        fib.append(fib[-1] + fib[-2])
        index += 1
    return index

print(nthDigitFibonacciNum(1000))
