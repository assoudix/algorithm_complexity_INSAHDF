#!/usr/bin/python3

def merge(ma_liste, l, m, r):
    """Tri à fusion (ou mergesort) - Logarithmic Complexity - Omar Assoudi"""
    iter1 = m - l + 1
    iter2 = r - m

    L = [0] * (iter1)
    R = [0] * (iter2)

    for i in range(0, iter1):
        L[i] = ma_liste[l + i]

    for j in range(0, iter2):
        R[j] = ma_liste[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < iter1 and j < iter2:
        if L[i] <= R[j]:
            ma_liste[k] = L[i]
            i += 1
        else:
            ma_liste[k] = R[j]
            j += 1
        k += 1

    while i < iter1:
        ma_liste[k] = L[i]
        i += 1
        k += 1


    while j < iter2:
        ma_liste[k] = R[j]
        j += 1
        k += 1



def mergeSort(ma_liste, l, r):
    if l < r:

        m = l+(r-l)//2

        mergeSort(ma_liste, l, m)
        mergeSort(ma_liste, m+1, r)
        merge(ma_liste, l, m, r)