#!/usr/bin/python3

def bulle(ma_liste):
    """Bubble sort algorithm - Quadratic Complexity - Omar Assoudi"""
    n = len(ma_liste)

    flag = False #pour détecter

    for i in range(n-1):
        for j in range(0, n-i-1):
            if ma_liste[j] > ma_liste[j + 1]:
                swap = True
                ma_liste[j], ma_liste[j + 1] = ma_liste[j + 1], ma_liste[j]

        if not swap:
            return
