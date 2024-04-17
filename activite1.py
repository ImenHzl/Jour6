def chaineCar(chain):
    nbrMaj=0
    nbrMin=0
    for i in chain:
        if i.isupper():
            nbrMaj+=1
        else:
            nbrMin+=1
    return(nbrMaj,nbrMin)

chaine="BonJour"
result=chaineCar(chaine)
print(f"(nombre Majuscule,nombre Miniscule)={result}")
