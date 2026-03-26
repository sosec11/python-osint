x=3 #il faut une valeur différente  de 0 pour rentrer dans la boucle
while(x!=0):
    x=int(input("Rentrer la valeur de x : "))
    resultat=x+2
    resultat=resultat*2
    print("Quand x vaut "+repr(x)+", le résultat vaut "+repr(resultat)+" !\n")
    if (resultat >0):
        print("Ce résultat est positif.")
    elif (resultat <0):
        print("Ce résultat est négatif.")
    else :
        print("Ce résultat est nul.")
    print("\n")

    print("Happy end !")