#------------------- on définit la fonction
def mafonction(t):
    """ Je mets ici le commentaire sur ma fonction.
C'est une fonction de la variable t.
Elle renvoie son image.
Ainsi, remarquez les points pour signaler que l'on ne travaille pas avec des entiers.
C'est plus prudent !"""
    image=2.*(t+2.)
    return image

#-------------------- le programme principal
"""Le programme va vous demander de choisir en bouche des valeurs de x.
Pour sortir, il suffira de choisir la valeur 0.
"""
x=3 #il faut une valeur différente de 0 pour rentrer dans la boucle
while(x!=0):
    x=int(input("Rentrer la valeur de x : "))
    resultat=mafonction(x)
    print("Quand x vaut "+repr(x)+", le résultat vaut "+repr(resultat)+" !\n")
    if (resultat >0):
        print("Ce résultat est positif.")
    elif (resultat<0):
        print("Ce résultat est négatif.")
    else :
        print("Ce résultat est nul.")
    print("\n")

print("Happy end !")