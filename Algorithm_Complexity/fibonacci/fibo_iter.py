#!/usr/bin/python3

def fibonacci_iter(n):
    "calcul de la suite de fibonacci avec iterations"

    if n == 0 or n == 1:
        return 1
    else:
        a=1
        b=1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c

        return c
