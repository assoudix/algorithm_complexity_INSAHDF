#!/usr/bin/python3

def position(str, c):

    for i in range(len(str)):
        if str[i] == c:
            return i
    return -1


#test
if __name__=="__main__":
    str='omar assoudi'
    print(position(str, 'm'))
