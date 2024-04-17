
def rotation_droite(liste, n):    #j'ai défini une fonction pour effectuer une rotation à droite d'une liste
    
    return liste[-n:] + liste[:-n]   # Effectue la rotation à droite en utilisant l'opération de slicing



liste_str = input("Entrez les éléments de la liste séparés par des espaces : ")   # Saisie de la liste par l'utilisateur
liste = liste_str.split()


n = int(input("Entrez le nombre de rotations à droite : "))    # Saisie du nombre de rotations par l'utilisateur


liste_rot = rotation_droite(liste, n)             # Appel de la fonction de rotation et affichage du résultat
print(f"Liste originale : {liste}")
print(f"Liste après rotation à droite de {n} positions : {liste_rot}")
