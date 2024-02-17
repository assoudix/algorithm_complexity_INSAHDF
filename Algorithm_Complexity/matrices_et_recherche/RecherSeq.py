#!/usr/bin/python3

def RechercheSeq(L,v):
    flag = False
    for i in L:
        if i == v:
            flag = True

    return flag

if __name__ == "__main__":
    L = [1, 2, 3, 4]
    v1 = 5
    v2 = 3
    print(RechercheSeq(L,v1))
    print(RechercheSeq(L,v2))
    print(L[len(L) - 1])