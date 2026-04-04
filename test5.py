try:
    n = int(input("Veuillez entrer un nombre entier: "))
except ValueError:
    print("Erreur: ce n'est pas un nombre entier.")
else:
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)
