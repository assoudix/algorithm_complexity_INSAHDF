#!/usr/bin/python3



def lomuto(ma_liste, deb, fin):
    """I opted for Lomuto cuz it's simple, complex method like Hoare can be faster"""

    pivot = ma_liste[fin]

    i = deb - 1

    for j in range(deb, fin):
        if ma_liste[j] <= pivot: #every element smaller than pivot goes to the right

            i = i + 1

            (ma_liste[i], ma_liste[j]) = (ma_liste[j], ma_liste[i])

    (ma_liste[i + 1], ma_liste[fin]) = (ma_liste[fin], ma_liste[i + 1]) #put pivot in the middle

    return i + 1 #pivot index

def Rapide(ma_liste, low, high):

    "Tri rapide avec schéma de partition Lomuto - on peut remplacer low et high par 0 et len(ma_liste)-1 respectivement"

    if low < high: #on vérifie que l'indice déb<fin

        pivot = lomuto(ma_liste, low, high) #partitionner la liste
        Rapide(ma_liste, low, pivot - 1) #recursion sur la première portion
        Rapide(ma_liste, pivot + 1, high) #idem sur la deuxième
