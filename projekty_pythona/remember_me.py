import json

# Wczytanie imienia z pliku, o ile wcześniej zostało w nim zapisane.
# W przeciwnym razie pytamy użytkownika o imię i zapisujemy je w pliku.
#filename = 'username.json'
#try:
    #with open(filename) as f:
        #username = json.load(f)
#except FileNotFoundError:
    #username = input("Jak masz na imię? ")
    #with open(filename, 'w') as f:
        #json.dump(username, f)
        #print(f"Twoje imię zostało zapisane i będzie używane później, {username}.")
#else:
    #print(f"Witamy ponownie, {username}!")
    



#def greet_user():
    #"""Przywitanie użytkownika z użyciem jego imienia."""
    #filename = 'username.json'
    #try:
        #with open(filename) as f:
            #username = json.load(f)
    #except FileNotFoundError:
        #username = input("Jak masz na imię? ")
        #with open(filename, 'w') as f:
            #json.dump(username, f)
            #print(f"Twoje imię zostało zapisane i będzie używane później, {username}.")
    #else:
        #print(f"Witamy ponownie, {username}!")
        
# Wywołanie funkcji greet_user()

#greet_user()

# 'Refaktoryzacja' - usprawnienie programu w celu podzielenie go na funkcje dla danej logiki programowej.

# Przeprowadzamy zatem refaktoryzację na funkcji greet_user():

import json

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
    if username: 
        print(f"Witamy ponownie, {username}!")  
    else:
        username = get_new_username()
        print(f"Twoje imię zostało zapisane i będzie używane później, {username}.")
 
#Wywołanie funkcji great_user()            
greet_user()            