#!/usr/bin/python3

def majuscule(str):
    "convertir str en maj"

    strlist=list(str)

    for i in range(len(strlist)):
        ascii_i = ord(strlist[i])
        strlist[i]=chr(ascii_i - 32)
    return "".join(strlist)

if __name__ == "__main__":
    str='omar assoudi'
    strfinal = majuscule(str)
    print(strfinal)
