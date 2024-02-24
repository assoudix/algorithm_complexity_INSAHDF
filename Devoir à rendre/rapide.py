#!/usr/bin/python3



def lomuto(ma_liste, deb, fin):
    """I opted for Lomuto because it's simple, complex method like Hoare can be faster"""

    pivot = ma_liste[fin]

    i = deb - 1

    for j in range(deb, fin):
        if ma_liste[j] <= pivot: #every element smaller than pivot goes to the right

            i = i + 1

            (ma_liste[i], ma_liste[j]) = (ma_liste[j], ma_liste[i])

    (ma_liste[i + 1], ma_liste[fin]) = (ma_liste[fin], ma_liste[i + 1]) #put pivot in the middle

    return i + 1 #pivot index

def Rapide(ma_liste, low, high):
    """Recursive quicksort using lomuto's partition - Logarithmic complexity - Omar Assoudi"""
    if low < high: #on vérifie que l'indice déb<fin

        pivot = lomuto(ma_liste, low, high) #Lomuto's partition can be replaced with a more elaborate schema (e.g. Hoare's)
        Rapide(ma_liste, low, pivot - 1) #First half recursion
        Rapide(ma_liste, pivot + 1, high) #Second half recursion
