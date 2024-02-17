#!/usr/bin/python3

def fibonacci(n):
    "calcul de la suite de fibonacci avec recurrence"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == "__main__":
    print(f"fibonacci(0) = {fibonacci(0)}")
    print(f"fibonacci(5) = {fibonacci(5)}")
    print(f"fibonacci(8) = {fibonacci(8)}")