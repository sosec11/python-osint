"""
Le programme va vous demander de choisir en bouche des valeurs de x.
Pour sortir, il suffira de choisir la valeur 0.
"""

x=3 #il faut une valeur différente de 0 pour rentrer dans la boucle
while(x!=0):
    x=int(input("Rentrer la valeur de x : "))
    resultat=x+2
    resultat=resultat*2
    print("Quand x vaut "+repr(x)+", le résultat vaut "+repr(resultat)+" !\n")

print("Happy end !")