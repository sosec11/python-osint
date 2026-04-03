try:
    n = int(input("Veuillez choisir un nombre entier : "))
except ValueError:
    print("Erreur : ce n'est pas un nombre entier")
else:
    if n > 0:
        print("Le nombre entré est positif.")
    elif n < 0:
        print("Le nombre entré est négatif.")
    else:
        print("Le nombre entré est zéro.")