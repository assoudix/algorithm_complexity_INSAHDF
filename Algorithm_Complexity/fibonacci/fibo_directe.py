#!/usr/bin/python3

import math

def fibonacci(n):
    """calcul direct fibonacci"""
    a = (1 + math.sqrt(5)) / 2
    b = (1 - math.sqrt(5)) / 2

    fibo = round((math.pow(a, n) - math.pow(b, n)) / math.sqrt(5))
    return fibo
