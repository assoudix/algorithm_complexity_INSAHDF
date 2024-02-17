#!/usr/bin/python3

from RecherSeq import RechercheSeq

def RechercheDic(L, v):

    #flag = False
    ind_deb = 0
    ind_fin = len(L) - 1
    #mil = (ind_deb + ind_fin)//2

    while ind_deb <= ind_fin:
        mil = (ind_deb + ind_fin)//2
        if (v == L[mil]):
            #flag = True
            return True
        elif (v > L[mil]):
            ind_deb=mil+1
        else:
            ind_fin = mil - 1

    return False


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    v1 = 5
    v2 = 22
    print(RechercheDic(L,v1))
    print(RechercheDic(L,v2))
