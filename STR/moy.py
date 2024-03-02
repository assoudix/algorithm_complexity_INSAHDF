#!/usr/bin/python3

from somme import somme

def moy(list):
    if len(list) == 0:
        print("liste vide")
        return
    else:
        return(somme(list)//len(list))


#test

if __name__=="__main__":
    liste = [1, 2, 3, 3, 1]
    moyenne = moy(liste)
    print(moyenne)