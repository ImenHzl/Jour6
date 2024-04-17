def additionner_nombres(nombre1_str, nombre2_str):

  try:
    # Convertir les chaînes de caractères en entiers
    nombre1 = int(nombre1_str)
    nombre2 = int(nombre2_str)
  except ValueError:
    # Gérer les erreurs de conversion (ex: chaînes non numériques)
    print(f"Erreur: Les valeurs saisies '{nombre1_str}' et '{nombre2_str}' ne sont pas des nombres valides.")
    return

  # Additionner les nombres
  somme = nombre1 + nombre2

  # Afficher le résultat de différentes manières
  print(f"La somme de {nombre1} et {nombre2} est : {somme}")
  print(f"Résultat en format chaîne : {str(somme)}")
  print(f"Résultat en format virgule flottante : {somme:.2f}")  # Afficher avec deux décimales

# Demander à l'utilisateur de saisir les nombres
nombre1_str = input("Entrez le premier nombre (sous forme de chaîne): ")
nombre2_str = input("Entrez le deuxième nombre (sous forme de chaîne): ")

# Appeler la fonction pour effectuer l'addition et afficher le résultat
additionner_nombres(nombre1_str, nombre2_str)
