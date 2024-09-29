""" 1000-Digit Fibonacci Number
--------------------------------
The Fibonacci sequence is defined by the recurrence relation: Fn = Fn−1 + Fn−2, 
where F1 = 1 and F2 = 1.
Find the index of the first term in the Fibonacci sequence to contain n digits. """

""" 1). Binet's Formula for the nth Fibonacci, Fn = (((1 + sqrt(5)) / 2)^n - ((1 - sqrt(5)) 
/ 2)^n) / sqrt(5).

2). This can be thought of as a function of the golden ratio, φ = (1 + sqrt(5)) / 2, and 
its inverse, ψ = (1 - sqrt(5)) / 2: Fn = φ^n / sqrt(5) - ψ^n / sqrt(5).

3). As n increases, ψ^n / sqrt(5) approaches 0. Therefore, Fn ~ φ^n / sqrt(5). This can 
be re written to estimate n: n ~ logφ (Fnsqrt(5)). Now, change to log(10): 
n ~ (log(Fn(sqrt(5)))) / logn = (log Fn + logsqrt(5)) / logφ. """

import math

def fib_term_index(n):
    phi = (1 + math.sqrt(5)) / 2
    return math.ceil(((n - 1) + math.log10(math.sqrt(5))) / math.log10(phi))

if __name__ == "__main__":
    print(fib_term_index(1000))
