
import json

# Wczytanie imienia z pliku, o ile wcześniej zostało w nim zapisane.
# W przeciwnym razie pytamy użytkownika o imię i zapisujemy je w pliku.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Jak masz na imię? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Twoje imię zostało zapisane i będzie używane później, {username}.")
else:
    print(f"Witamy ponownie, {username}!")