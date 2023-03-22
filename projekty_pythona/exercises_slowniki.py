# Zrób to sam 

# Ćw 6.1 Osoba

# Tworzymy słownik:

elon_musk = {
	'first_name': 'Elon',
	'last_name': 'Musk',
	'age': 37,
	'city': 'Waszynkton'
}
print(elon_musk) # Wyświetlenie słownika

# Ćw 6.2 Ulubione liczby

ulubione_cyfry = {
	'Kamil': 7,
	'Kasia': 13,
	'Magdalena': 9,
	'Krzysztof': 11,
	'Maria': 2
}
print(ulubione_cyfry)
print(f"Ulubioną cyfrą Magdy jest {ulubione_cyfry['Magdalena']}.")

# Ćw 6.3 Glosariusz 

glosariusz = {
	'pętla': 'Metoda pozwalająca wykonać daną operację kilku krotnie.',
	'iteracja': 'Metoda, która przeprowadza daną operację dla każdego elementu po kolei.',
	'słownik': 'Zbiór danych zawierających klucz - wartość.',
	'lista': 'Zbiór elemenentów lub cyfr zamieszczonych między nawiasami klamrowymi, które można edytować albo nadpisywać.',
	'krotka': 'Elementy w nawiasach okrągłych, których wartość jest przypisywana stale i nie można ich edytować.',
	'metoda items()': 'Wywołuje wszystkie elementy klucz-wartość.',
	'metoda keys()': 'Wywołuje tylko klucze w słowniku.',
	'metoda values()': 'Wywołuje tylko wartości w słowniku.',
	'funkcja sorted()': 'Sortuje elementy rosnąco.',
}
print(glosariusz)

# Zrób to sam

# Ćw 6.4 Glosariusz 2

for name,opis in glosariusz.items():
	print(f"\n {name.title()}:")
	print(f"\n{opis}")

# Ćw 6.5 Rzeki 

rzeki = {
	'nil': 'egipt',
	'wisła': 'polska',
	'perlaga': 'włochy',
}

for miejsce,rzeka in rzeki.items():
	print(f"\n{rzeka.title()} przepływa przez {miejsce.title()}.")

# Wszystkie nazwy rzek:
print("Wszystkie rzeki to:\n")
for rzeka in rzeki.keys():
	
	print(f"{rzeka.title()},")

# Wszystkie państwa:
print("Wszystkie państwa to:\n")
for miejsce in rzeki.values():
	print(f"{miejsce.title()},")		

# Ćw 6.6 Ankieta 

favourite_languages = {
	'janek': 'python', 
	'sara': 'c',
	'mikołaj': 'ruby',
	'andrzej': 'python',
	'paweł': 'c++'
}

ankieta = ['janek','sebastian','marcin','sara']

for imie in sorted(favourite_languages.keys()):
	if imie in ankieta:
		print(f"{imie.title()}, dzięujemy za udział w naszej ankiecie!")
	else:
		print(f"{imie.title()}, koniecznie weź udział w naszej ankiecie!")		