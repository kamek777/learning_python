# Osobiste powitanie 
imie = "Eryk"
print(f"Witaj, {imie}! Czy chcesz dzisiaj poznawać Pythona?")
# Wielkość liter w imionach
imie = "Kamil"
print("małe litery:", imie.lower())
print("wielkie litery:",imie.upper())
print("wielka litera na początku:", imie.title())
# Sławny cytat 
print('Marek Aureliusz powiedział kiedyś: "Nasze życie jest takik, jakim uczyniły je nasze myśli."')
# Sławny cytat 2
famous_person = "Marek Aureliusz"
message = f'{famous_person} powiedział kiedyś: "Nasze życie jest takik, jakim uczyniły je nasze myśli."'
print(message)
# Usunięcie białych znaków z imienia
name = " Marek Aureliusz\n\t"
print(name.lstrip())
print(name.rstrip())
print(name.strip())