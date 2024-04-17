# Demander de saisir le premier nombre ( sous forme de chaîne de caractères)
nombre1_str = input("Entrez le premier nombre: ")

# Demander de saisir le deuxième nombre ( sous forme de chaîne de caractères)
nombre2_str = input("Entrez le deuxième nombre: ")

# Convertir les chaînes de caractères en nombres entiers
try:
  nombre1 = int(nombre1_str)
  nombre2 = int(nombre2_str)
except ValueError:
  print("Erreur: Veuillez saisir uniquement des nombres entiers.")
  exit()  # Quitter le programme si la conversion échoue

# Effectuer l'addition des nombres
somme = nombre1 + nombre2

# Afficher le résultat
print(f"La somme de {nombre1} et {nombre2} est : {somme}")
