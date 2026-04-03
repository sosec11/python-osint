try:
    n = int(input("Veuillez choisir un nombre entier : "))
except ValueError:
    print("Erreur : ce n'est pas un nombre entier")

if n % 2 == 0:
    type_nombre = "pair"
else:
    type_nombre = "impair"

if n > 0:
    signe = "positif"
elif n < 0:
    signe = "négatif"
else:
    signe = "zéro"

print(f"Le nombre entré est {type_nombre} et {signe}.")