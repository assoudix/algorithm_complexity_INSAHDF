#!/usr/bin/python3

"""def maximum(list):

    if len(list) == 0:
        print("liste vide")
        return


    else:
        max = list[0]
        for number in list:
            if number > max:
                max = number
        return max"""


def maximum_r(liste):

    if len(liste) == 0:

        return 0

    else:

        max_rest = maximum_r(liste[1:])

        if max_rest is None:
            return liste[0]

        return max(liste[0], max_rest)


if __name__== "__main__":
    liste = [1, 2, 77, 3, 1]
    max = maximum_r(liste)
    print(max)