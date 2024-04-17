import random

def devineNombre():

    nombre_aleatoire = random.randint(1, 100)
    print(nombre_aleatoire)
    limite=5
    i=1
    while i<= limite:
        nombre_alt=input("Devine le nombre:")
        if int(nombre_alt) >= int(nombre_aleatoire):
            print("Le nombre est plus petit")
        else:
            print("le nombre est plus grand")  
        i+=1

result=devineNombre()
