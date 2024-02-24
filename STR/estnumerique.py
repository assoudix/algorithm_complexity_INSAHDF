#!/usr/bin/python3

def estnumerique(str):
    for i in str:
        if i not in "0123456789":
            return False

    return True


if __name__=="__main__":
    str1='omar 120297'
    str2='120297'
    print(estnumerique(str1))
    print(estnumerique(str2))