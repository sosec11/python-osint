word = input("Enter a word: ").lower()

vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print(f"Number of vowels: {count}")