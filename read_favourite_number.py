# Program wyświetlający ulubioną liczbę podaną przez użytkownika w pliku favoutive_number.json

import json

filename = 'favourite_number.json'

with open(filename) as f:
        number = json.load(f)
        print(f"Znam Twoją ulubioną liczbę, to {number}")
