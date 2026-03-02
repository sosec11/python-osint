print("Hello!")



print("Salut!")
nombre_utilisateur = input("Combien y a-t-il de personnes avec toi? : ")

# L'index (souvent abrégé "i") va permettre de compter le nombre d'itérations de la boucle
index = 0

# Boucle basée sur le nomnre d'utilisateurs
# Par défaut, le type renvoyé par la fonction "input" est une "string"
# Nous devons la convertir en int grâce à la syntaxe "int(variable)"
while index < int(nombre_utilisateur):
    nom_utilisateur = input("Comment t'appelles-tu? : ")
    print(f"Enchanté {nom_utilisateur}, moi c'est Script!")

    # Récupération de la longeur du prénom avec la fonction "len()"
    longeur_prenom = len(nom_utilisateur)
    if longeur_prenom > 5:
    print(f"Ton prénom fait {longeur_prenom} caractères, c'est plutôt long!")
else:
    print(f"Ton prénom fait {longeur_prenom} caractères, c'est plutôt court!")

    # Nous arrivons à la fin d'une boucle, nous devons incrémenter (ajouter 1)
    # à l'index pour éviter une boucle infinie
    index += 1

# On adapte notre "au revoir" en fonction du nombre de personnes
if int(nombre_utilisateur) > 1:
    print("Au revoir tout le monde!")
else:
    print("Au revoir!")