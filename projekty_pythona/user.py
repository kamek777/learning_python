# Iteracja przez słowniki
# Tworzymy losowy słownik
user_0 = {
	'username': 'kamil007',
	'first': 'Kamil',
	'last': 'Kwiek',
}

# Iterujemy przy użyciu pętli for
for key,value in user_0.items():
	print(f"\nKlucz: {key}")
	print(f"Wartość: {value}")

# Metoda items() pozwala zwrócić wartość listy par klucz - wartość.

# Inny przykład 

favourite_languages = {
	'janek': 'python', 
	'sara': 'c',
	'mikołaj': 'ruby',
	'andrzej': 'python',
}

for name, language in favourite_languages.items():
	print(f"Ulubionym językiem programowania użytkownika {name.title()} jest {language}.")	

# Iteracja przez same klucze przy użyciu metody keys()

for name in favourite_languages.keys():
	print(name.title())

# Tak samo zadziała, bez użycia metody keys()

for name in favourite_languages:	
	print(name.title())


# Specjalne użycie słownika

favourite_languages = {
	'janek': 'python', 
	'sara': 'c',
	'mikołaj': 'ruby',
	'andrzej': 'python',
	'paweł': 'c++'
}

# Tworzymy listę przyjaciół

friends = ['paweł', 'sara']

for name in favourite_languages.keys():
	print(f"Witaj, {name.title()}.")

	if name in friends:
		lang = favourite_languages[name].title()
		print(f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym językiem jest {lang}!")


# Sprawdzenie czy dana osoba, wzięła udział w ankiecie:
if 'ela' not in favourite_languages.keys():
 	print("Ela, weź proszę udział w ankiecie!")

 # Sortowanie słownika
 
for name in sorted(favourite_languages.keys()):
	print(f"{name.title()}, dziękuję za udział w ankiecie.")
 		
# Iteracja przez same wartości w słowniku przy użyciu metody values()

for lang in favourite_languages.values():
	print(lang.title())

# Funkcja set() wyświetla tylko unikatowe elementy bez powtarzania:

for lang in set(favourite_languages.values()):
	print(lang.title())	