import math
import random

print(math.sqrt(16))

# Calcul de la racine carrée
nombre = 16
racine = math.sqrt(nombre)
print(f"La racine carrée de {nombre} est {racine}")

# Utilisation de la constante (variable non modifiable) pi
rayon = 5
aire = math.pi * rayon**2
print(f"L'aire d'un cercle de rayon {rayon} est {aire:.2f}")

# Calcul du factoriel
n = 5
factoriel = math.factorial(n)
print(f"Le factoriel de {n} est {factoriel}")

# Générer un nombre entier aléatoire entre 1 et 10
nombre_aleatoire = random.randint(1, 10)
print(f"Nombre aléatoire généré: {nombre_aleatoire}")

# Sélectionner un élément aléatoire dans une liste
fruits = ["pomme", "banane", "cerise", "orange"]
fruit_choisi = random.choice(fruits)
print(f"Fruit choisi au hasard: {fruit_choisi}")

# Mélanger une liste
random.shuffle(fruits)
print(f"Liste mélangée: {fruits}")