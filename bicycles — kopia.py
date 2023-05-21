# Tworzymy listę
bicycles = ['trekingowy','górski', 'miejski', 'szosowy']
print(bicycles)
# wyświetlanie pierwszego elementu z listy
print(bicycles[1])
# Wyświetlamy pierwsy element z listy i dodajemy wielką literę na początku do tego wyrazu
print(bicycles[0].title())
# Zwracanie ostatniego elementu z listy
print(bicycles[-1])
# Zwracanie trzeciego od końca elementu
print(bicycles[-3])
# Zwracanie drugiego elementu od końca
print(bicycles[-2])

# Tworzenie ciągów znaków z wykorzystaniem listy
message = f"Moim ulubionym rowerem jest rower {bicycles[1].title()}"
print(message)