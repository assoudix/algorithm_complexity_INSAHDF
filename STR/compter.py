#!/usr/bin/python3

def compter(str, c):
    """compter les occurences de c dans str"""
    count = 0
    for i in str:
        if i == c:
            count +=1
    return count


#test

if __name__ == "__main__":
    str = 'omar assoudi'
    print(compter(str, 'o'))