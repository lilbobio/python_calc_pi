import sys
from decimal import *

if len(sys.argv) != 2:
    print("usage: python calc.py <digit>")
    sys.exit(1)

max_digit = int(sys.argv[1])

getcontext().prec = max_digit + 10

k = 0

def factorial(n : int):
    i = 1
    while n > 0:
        i = i * n
        n = n -1
    return i
        
pi = 0

term = int(max_digit/14)

while k <= term:
    current_digit = Decimal(((-1)**k) * factorial(6*k) * (545140134*k + 13591409))
    current_digit = current_digit / Decimal(factorial(3*k) * Decimal(factorial(k)**3) * Decimal(640320)**(3*k+Decimal(3/2)))
    
    pi = pi + current_digit
    k = k + 1

pi = pi * 12

pi = Decimal(1)/pi



print(round(pi, max_digit))