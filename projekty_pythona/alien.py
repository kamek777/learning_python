# Tworzymy słowniki
alien_0 = {'color': 'zielony', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Dodanie nowej pary klucz-wartość:

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Pusty słownik

alien_1 = {} # pisty słownik
alien_1['color'] = 'zielony'
alien_1['points'] = 5
print('Alien 1:', alien_1)

# Edycja słownika

print(f"Obcy ma kolor {alien_1['color']}.")
alien_1['color'] = 'czerwony'
print(alien_1)
print(f"Obcy ma teraz kolor {alien_1['color']}.")


# Usuwanie elementu ze słownika:
alien_2 = {'color': 'zielony', 'points': 10}
del alien_2['points']
print(alien_2)

# Przy użyciu metody get() możemy uniknąć błędu, gdy słownik nie będzie zawierał konkretnej wartości jaką chcemy:

alien_3 = {'color': 'zielony', 'speed': 'wolno'}
point_value = alien_3.get('points', 'Brak przypisanych punktów.')
print(point_value)
