# Zrób to sam 
# Ćw 3.8 Zwiedzaj świat
miejsca = ['Paryż', 'Londyn', 'Wyspy Karaibskie','Malediwy']
print(miejsca)
# Używając funkcji sorted(), sortujemy rosnąco listę, lecz nie zmieniamy jej oryginalnego ułożenia
print(sorted(miejsca))
# Sprawdzenie powyższej tezy
print(miejsca)
# Zmiana kolejności elementów w liście przy pomocy funkcji reverse()
miejsca.reverse()
print(miejsca)
# Jeśli chcemy spowrotem zmienić kolejność elementów w liście do stanu początkowego, ponawiamy kod
miejsca.reverse()
print(miejsca)
# Ok
# Sortujemy rosnąco listę
miejsca.sort()
print(miejsca)
# Sortujemy malejąco listę 
miejsca.sort(reverse=True)
print(miejsca)

# Korzystając z listy z poprzedniego zadania
# Sprawdzanie długości listy funkcją len()
goscie = ["marek aureliusz", "adam małysz", "jan nowak"]
print(len(goscie))
print(f"Liczba gości zaproszonych na współny obiad wynosi {len(goscie)}.")

# Ćw 3.10 Każda funkcja
lista = []
lista.append('Wisła')
print(lista)
lista.insert(1,'Odra')
print(lista)
lista.append('Niemcy')
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)
