# Ćwiczenia 
names = ['Paweł', "Łukasz", "Marcin", "Iwona"]
# Wyświetlamy odpowiednio kolejne elementy z listy
print(names[0])
print(names[1])
print(names[2])
print(names[3])
# Wyswietlanie odpowienich elementów z listy oraz przypisywanie im wielkich liter na początku
print(f"Witam serdecznie, {names[0].title()}!")
print(f"Witam serdecznie, {names[1].title()}!")
print(f"Witam serdecznie, {names[2].title()}!")
print(f"Witam serdecznie, {names[3].title()}!")
# Tworzymy listę z środkami transportu i generujemy zdania związane z tymi elementami
srodki_transportow = ["motocykl","rower","tramwaj", "pociag"]
print(f"Ostatnio miałem możliwość przejechać się takim sprzętem jak {srodki_transportow[0]}.")
print(f"Chciałbym mieć {srodki_transportow[1]}.")
print(f"Moim marzeniem jest swój {srodki_transportow[2]}.")
print(f"{srodki_transportow[3].title()} zawsze robił na mnie ogromne wrażenie pod względem wielkości.")

# Dodawanie elementu do listy na pozycji ostatniej
motocyrcles = ['honda','yamaha','suzuki']
motocyrcles.append('ducati')
print(motocyrcles)
# Wstawianie elementów na listę poprzez dodanie argumentu indeksu oraz nazwy 
motocyrcles.insert(0,'bmw')
print(motocyrcles)

# Usunięcie elementu z listy za pomocą polecenia 'del' poprzez dodanie w argumencie indeksu
del motocyrcles[0] # usuwa pierwszy element z listy
print(motocyrcles)

# Usunięcie elementu za pomocą funkcji pop()
poppep_motocyrcles = motocyrcles.pop() # usuwa ostatni element ale NIE permamentcie tak jak w przypadku polecenia del.
print(poppep_motocyrcles)
# Usunięcie dowolnego elementu z listy 
first_owned = motocyrcles.pop(0) # W argumencie funkcji pop() podajemy wartość indeksu
print(first_owned)

# Jeżeli chcesz tylko usunąć element z listy wybierz polecenie 'del' natomiast jeśli chcesz ten element gdzieś później wykorzystaj to zastosuj funckję pop().

# Usunięcie elementu na podstawie wartości
motocyrcles.remove('suzuki') # Usuwamy 'suzuki'
print(motocyrcles)
