#!/usr/bin/python3

def traduire(st, dico):
    mots = list(st.split(" "))

    for i in range(len(mots)):
        if mots[i] in dico.keys():
            mots[i] = dico[mots[i]]
        else:
            pass

    traduit = " ".join(mots)
    return traduit

if __name__ == "__main__":
    d = {"hello": "bonjour", "world": "monde"}
    st= "hello world"
    print(traduire(st, d))
    #L=[3,8]
