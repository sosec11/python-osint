word = input("Veuillez entrer un mot pour vérifier si c'est un palindrome: ")

if word == word[::-1]:
    print("Ce mot est un palindrome.")
else:
    print("Ce mot n'est pas un palindrome.")