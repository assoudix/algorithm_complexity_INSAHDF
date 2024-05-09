#!/usr/bin/python3
def genereralphabmaj():
    L=[]
    for i in range (65, 91):
        L.append(chr(i))
    return L

if __name__=="__main__":
    L=genereralphabmaj()
    print(L)
