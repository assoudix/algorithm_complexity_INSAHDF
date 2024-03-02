#!/usr/bin/python3

'''
écriture:

#!/usr/bin/python3

f = open("fichiers/hello", "w")
L=["hello", "world"]
f.writelines(L)
f.close.

'''

#Lecture:

f = open("fichiers/hello", "r")
c = f.readline(4)
d = f.readline()
print(c)
print(d)
f.close

print(c)

print(d)