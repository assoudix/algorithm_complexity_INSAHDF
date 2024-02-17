#!/usr/bin/python3

def SommeMat(m1, m2):
    if len(m1) != len(m2):
        print("matrices incompatibles")
        return

    if len(m1[0]) != len(m2[0]):
        print("matrices incompatibles")
        return
