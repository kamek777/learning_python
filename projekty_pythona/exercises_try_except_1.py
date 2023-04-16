# Zrób to sam 

# Ćw 10.11. Ulubiona liczba

import json

def favourite_number():
    """Program prosi użytkownika o ulubioną liczbę i zapisuje ją w pliku JSON."""
    number = input("Podaj swoją ulubioną liczbę: ")
    filename = 'favourite_number.json'
    with open (filename, 'w') as f:
        json.dump(number, f)
    return number

# Wywołanie funkcji 

#favourite_number()

# Ćw 10.12. Zapamiętana ulubiona liczba

filename = 'favourite_number.json'

try:
    with open(filename) as f:
            number = json.load(f)
            print(f"Znam Twoją ulubioną liczbę, to {number}")
except FileNotFoundError:
    number = input("Podaj swoją ulubioną liczbę: ")
    filename = 'favourite_number.json'
    with open (filename, 'w') as f:
        json.dump(number, f)
        
# Ćw 10.13. Weryfikacja użytkownika

def get_stored_username():
    """Pobieranie imienia z pliku, o ile taki istnieje."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Poproszenie użytkownika, aby podał swoje imię, a następnie zapisanie tego imienia w pliku."""
    username = input("Jak masz na imię? ")
    filename = 'username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
    return username

def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""  
    username = get_stored_username()
    question = input(f"Czy {username} to Twoje imię? Jeśli tak napisz 'yes' lub 'no'.")
    if question == 'yes': 
        print(f"Witamy ponownie, {username}!")  
    elif question == 'no':
        username = get_new_username()
        print(f"Twoje imię zostało zapisane i będzie używane później, {username}.")
            
greet_user()                

    
    
    
    