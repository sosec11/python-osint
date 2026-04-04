try:
    n = int(input("Veuillez choisir un nombre entier: "))
except:
    print("Erreur : ce n'est pas un nombre")
else:
    if n%2 == 0:
        print("Nombre pair")
    else:
        print("Nombre impair")