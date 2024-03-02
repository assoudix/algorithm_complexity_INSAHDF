#!/usr/bin/python3

def somme(list):
    sum = 0
    if len(list) == 0:
        print("liste vide")
        return
    else:
        for number in list:
            sum = sum + number
        return sum

#test

if __name__=="__main__":
    liste = [1, 2, 3, 3, 1]
    somme_liste = somme(liste)
    print(somme_liste)