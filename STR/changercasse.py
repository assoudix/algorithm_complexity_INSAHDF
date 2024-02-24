#!/usr/bin/python3

def change(str):

    strlist=list(str)

    for i in range(len(strlist)):
        ascii_i = ord(strlist[i])
        #ord('a')<=ord(ascii)<=ord('z')
        #'a'<=ascii<='z'

        if ascii_i >= ord('a') and ascii_i <= ord('z'):
            strlist[i]=chr(ascii_i - 32)
        elif ascii_i > ord('A') and ascii_i < ord('Z'):
            strlist[i]=chr(ascii_i + 32)
    return "".join(strlist)

if __name__ == "__main__":
    str='oMaR aSsouDi'
    strfinal = change(str)
    print(strfinal)
