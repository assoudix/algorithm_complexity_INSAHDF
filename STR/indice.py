#!/usr/bin/python3

def indice(liste, elem):

    for i in range(len(liste)):
        if liste[i] == elem:
            return i+1
    return -1

if __name__== "__main__":
    liste = [1, 2, 77, 3, 1]
    ind = indice(liste, 87)
    print(ind)