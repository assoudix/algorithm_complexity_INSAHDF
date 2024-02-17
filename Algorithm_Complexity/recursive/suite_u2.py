#!/usr/bin/python3

def fonction_u2(n):
    if n == 0:
        return 1
    else:
        u = fonction_u2(n-1)
        if u != 0:
            return 2*(u+2/u)


if __name__ == "__main__":
    n=30
    print(fonction_u2(n))