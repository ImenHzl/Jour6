def chaineCar(chain):
    nbrMaj=0
    nbrMin=0
    for i in chain:
        if i.isupper():
            nbrMaj+=1
        else:
            nbrMin+=1
    return nbrMaj,nbrMin

chaine=input("entrez une chaine de caractère: ")
maj,min=chaineCar(chaine)
print(f"nombre Majuscule:{maj}")
print(f"nombre Miniscule:{min}")
