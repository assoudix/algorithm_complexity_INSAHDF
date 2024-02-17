#!/usr/bin/python3

def fonction_u1_r(n):
    if n==0:
        return 1
    else:
        u=1
        for i in range(1,n+1):
            u = 2*(u+(2/u))
        return u

#test

if __name__ == "__main__":
    n=30
    print(fonction_u1_r(n))