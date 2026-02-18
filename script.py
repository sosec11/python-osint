print("OSINT script started")

email = ["test@gmail.com", "admin@yahoo.com", "fake-email"]

for email in email:
    valid = "@" in email and "." in email
    print(email, "=>", "OK" if valid else "INVALID")