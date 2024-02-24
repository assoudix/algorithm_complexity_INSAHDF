#!/usr/bin/python3

def caractere(a, b):
    if b<a:
        print("erreur: b doit etre supérieur à a")
    elif a<0:
        print("erreur: a négatif")
    else:
        for i in range(a+1, b): #a exclu
            print(chr(i), end ="-")

#test

if __name__=="__main__":
    a=5
    b=55
    caractere(a,b)