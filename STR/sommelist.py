#!/usr/bin/python3

def sommelist(lst1, lst2):
    n = len(lst1)
    m = len(lst2)

    if n != m:
        print("listes de tailles differentes")
        return None

    else:
        newlist = [0]*n
        for i in range(n):
            newlist[i] = lst1[i] + lst2[i]

        return newlist


if __name__=="__main__":
    liste1 = [1, 2, 3, 4, 5]
    liste2 = [5, 4, 3, 2, 1]
    somme_liste = sommelist(liste1, liste2)
    print(somme_liste)