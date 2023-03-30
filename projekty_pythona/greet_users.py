# Przekazywanie listy

def greet_users(names):
    """Wyświetla proste powitanie każdemu użytkownikowi z listy."""
    for name in names:
        msg = f"Witaj,{name.title()}!"
        print(msg)

usernames = ['błażej', 'tymek', 'alicja']
greet_users(usernames) 
   