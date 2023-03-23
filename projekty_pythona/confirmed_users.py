unconfirmed_users = ['alicja','bartek','kasia']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    
    print(f"Weryfikacja użytkownika: {current_users.title()}")
    confirmed_users.append(current_users)
    
print("\nZweryfikowano wymienionych poniżej użytkowników:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())    