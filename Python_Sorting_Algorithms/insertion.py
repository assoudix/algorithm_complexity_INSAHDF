#!/usr/bin/python3

def insertion(ma_liste):
    """Insertion sort algorithm - Quadratic Complexity - Omar Assoudi"""
    n = len(ma_liste)

    for i in range(1, n):  #Select an element from the list
        inserted_elem = ma_liste[i]  #The element to be inserted
        j = i-1
        while j >= 0 and inserted_elem < ma_liste[j]: #Sort on the left side
            ma_liste[j+1] = ma_liste[j]  # Shift elements to the right
            j -= 1
        ma_liste[j+1] = inserted_elem