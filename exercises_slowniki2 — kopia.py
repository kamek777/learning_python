# Zró to sam 

# Ćw 6.7 Osoby 

elon_musk = {
	'first_name': 'Elon',
	'last_name': 'Musk',
	'age': 37,
	'city': 'Waszynkton',
}

leo_messi = {
	'first_name': 'Lionel',
	'last_name': 'Messi',
	'age': 32,
	'city': 'Barcelona',
}

cris_ronaldo = {
	'first_name': 'Cristiano',
	'last_name': 'Ronaldo',
	'age': 34,
	'city': 'Madryt',
}

people = [elon_musk,leo_messi,cris_ronaldo]
for person in people:
	print(person)

# Ćw 6.8 Zwierzęta

dog = {
	'wzrost': 60,
	'waga': 20,
	'imie': 'daisy',
	}	

cat = {
	'wzrost': 35,
	'waga': 8,
	'imie': 'miałczek',
	}		

horse = {
	'wzrost': 180,
	'waga': 120,
	'imie': 'iskra',
}	

pets = [dog,cat,horse]
for pet in pets:
	print(pet)

# Ćw 6.9 Ulubione miejsca 

favorite_places = {
	'kamil': ['paryż','londyn','karaiby'],
	'michał':['siemiechów','gromnik','zakliczyn'],
	'kacper': ['tarnów','tuchów', 'kraków'],
	}	

for imie, miejsca in favorite_places.items():
	print(f"Ulubionym miejscem użytkownika {imie.title()} jest:")
	for miejsce in miejsca:
		print(f"\t{miejsce.title()}")

# Ćw 6.10 Ulubione liczby 

ulubione_cyfry = {
	'Kamil': 7,
	'Kasia': 13,
	'Magdalena': 9,
	'Krzysztof': 11,
	'Maria': 2
}

# Edytowanie elementów w słowniku

ulubione_cyfry = {'Kamil': 7, 'Kasia': 11, 'Magdalena': [10,8,1],'Krzysztof': 23, 'Maria': 123}
print(ulubione_cyfry)

# Ćw 6.11 Miasta

cities = {
	'Kraków':{
		'wojewodztwo': 'małopolskie',
		'wielkosc': 240,
		'herb': 'smok',

		},
	'Wrocław':{
		'wojewodztwo': 'pomorskie',
		'wielkosc': 245,
		'herb': 'łoś',

		},
	'Zakopane':{
		'wojewodztwo': 'małopolskie',
		'wielkosc': 190,
		'herb': 'ryś',

		},
}

for miasto, fakty in cities.items():
	print(f"Miasto: {miasto.title()}")
	fakty = f"Województwo to {fakty['wojewodztwo']}, Herb to{fakty['herb']}, Wielkość to {fakty['wielkosc']}"

	print(f"Informacje o mieście: {fakty.title()}")


# Ćw 6.12 Rozszerzenia 

aliens = []
for alien in range(10):
	new_alien = {'color': 'zielony', 'points': 10 }
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'zielony':
		alien['color'] = 'czerwony'
		alien['points'] = 5



for alien in aliens[3:9]:
	if alien['color'] == 'zielony':
		alien['color'] = 'żółty'
		alien['points'] = 20


for alien in aliens:
	print(alien)

