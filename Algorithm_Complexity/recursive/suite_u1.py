#!/usr/bin/python3

def fonction_u1(n):
    if n == 0:
        return 1
    elif fonction_u1(n-1) != 0:
        return ((2*fonction_u1(n-1)+2)/fonction_u1(n-1))

if __name__ == "__main__":
    n=30
    print(fonction_u1(n))