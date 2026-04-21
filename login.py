correct_username = "admin"
correct_password = "Password123"

attempts = 3

while attempts > 0:
    username = input("Nom d'utilisateur : ")
    password = input("Mot de passe : ")

    if username == correct_username and password == correct_password:
        print("Connexion réussie")
        break
    else:
        attempts -= 1
        print(f"Identifiants incorrects. Tentatives restantes : {attempts}")

if attempts == 0:
    print("Accès bloqué")