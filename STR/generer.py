#!/bin/python3
from random import randint
import matplotlib.pyplot as plt

def generer(n, a, b):
    liste=[0]*n
    for i in range(n):
        liste[i] = randint(a, b)

    return liste

if __name__=="__main__":
    #ma_liste=generer(5,1,9)
    #print(ma_liste)

    #Simulation de n lancers d'un dé à 6 faces:

    simulation_liste = generer(60, 1, 6)
    #print("\n\nLa simulation du lancement du dé 6 fois est:  " + str(simulation_liste))
    compt0 = compt1 = compt2 = compt3 = compt4 = compt5 = 0

    for number in simulation_liste:

        if number == 1:
            compt0 += 1
        elif number == 2:
            compt1 +=1
        elif number == 3:
            compt2 +=1
        elif number == 4:
            compt3 +=1
        elif number == 5:
            compt4 +=1
        else:
            compt5 +=1
print("\nLe nombre des occurences par élément:\n")
print("\nNombre d'occurences de 1: " + str(compt0))
print("\nNombre d'occurences de 2: " + str(compt1))
print("\nNombre d'occurences de 3: " + str(compt2))
print("\nNombre d'occurences de 4: " + str(compt3))
print("\nNombre d'occurences de 5: " + str(compt4))
print("\nNombre d'occurences de 6: " + str(compt5))

#courbe:


x = [1,2,3,4,5,6]
y= [compt0, compt1, compt2, compt3, compt4, compt5]

plt.hist(y, bins=6)

plt.xlabel('Faces du dé')
plt.ylabel('Nombre occurence')


plt.title('Lancement dé à 6 faces')

plt.savefig("courbe.png")