aliens = []
for alien in range(10):
	new_alien = {'color': 'zielony', 'points': '5', 'speed': 'wolno'}
	aliens.append(new_alien)


	

for alien in aliens[0:3]:
	if alien['color'] == 'zielony':
		alien['color'] = 'niebieski'
		alien['speed'] = 'średnio'
		alien['points'] = 10

for alien in aliens[:5]:
	print(alien)
	print("...")

# Zagnieżdżanie list w środku słowników 

favorite_languages = {
	'janek': ['python','ruby'],
	'sara': ['c'],
	'edward': ['ruby','go'],
	'paweł': ['python', 'haskell'],
}	

for name,langs in favorite_languages.items():
	print(f"\n Ulubione języki programowania użytkownika {name.title()} to:")
	for lang in langs:
		print(f"\n{lang.title()}")

# Zagnieżdżenie słownika w słowniku:

users = {
	'aeinstein':{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie':{
		'first': 'maria',
		'last': 'skłodowska-curie',
		'location': 'paryż',	
		},

}

for username,user_info in users.items():
	print(f"Nazwa użytkownika {username}.")	
	full_name = f"{user_info['first']} {user_info['last']}"
	location = f"{user_info['location']}"

	print(f"\t Imię i nazwisko to: {full_name.title()}.")
	print(f"Miejscowość: {location.title()}")
	