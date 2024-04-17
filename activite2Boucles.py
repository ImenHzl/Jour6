#Affiche une pyramide d'étoiles de la hauteur spécifiée.

def creer_pyramide_etoile(hauteur):      # Définition de la fonction pour créer une pyramide d'étoiles

  if hauteur <= 0:    # Vérifier si la hauteur est valide
    print("Erreur: La hauteur doit être un nombre entier positif.")
    return

  for etage in range(1, hauteur + 1):     # Boucle pour créer chaque étage de la pyramide

    espaces = " " * (hauteur - etage)    #calculer le nombre d'espaces nécessaires pour aligner les étoiles de l'étage.

    etoiles = "*" * (2 * etage - 1)      #calculer le nombre d'étoiles à afficher. (2*etage -1 pour assurer d'obtenir un nombre impair d'étoiles)

    print(espaces + etoiles) # Afficher l'étage de la pyramide


hauteur_str = input("Entrez la hauteur de la pyramide (c'est le nombre d'étages): ")  # Demander à l'utilisateur la hauteur de la pyramide

try:                                    #  gérer les erreurs
    hauteur = int(hauteur_str)           # Convertir la hauteur en entier
except ValueError:
    print("Erreur: La hauteur doit être un nombre entier.")
    exit()


creer_pyramide_etoile(hauteur)   # appeler la function pour creer et afficher la pyramide
