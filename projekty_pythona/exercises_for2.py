# Zrób to sam 

# Ćw 5.3 Kolory obcych, część 1.
alien_colour = 'czarny'
if alien_colour == 'zielony':
	print("")
if alien_colour == 'czarny':
	print("Zarobiłeś 5 pkt!")	

# Ćw 5.4 Kolory obcych, część 2.
alien_colour2 = 'zielony'
if alien_colour2 == 'zielony':
	print("Zarobiłeś 5 pkt!")
elif alien_colour2 != 'zielony':
	print("Dostałeś 10 pkt za zestrzelenie obcego!")

# Ćw 5.5 Kolory obcych, część 3.
alien_colour3 = 'czerwony'
if alien_colour3 == 'żółty':
	print('Masz 10 pkt!')
elif alien_colour3 == 'zielony':
	print('Masz 5 pkt!')
elif alien_colour3 == 'czerwony':
	print('Masz 15 pkt!')


# Ćw 5.6 Etapy życia.
age = 22 
if age < 2 and age < 4:
	print("Jesteś dzieckiem, który uczy się chodzić.")
elif age > 4 and age <13:
	print("Jesteś dzieckiem.")
elif age > 13 and age < 20:
	print("Jesteś nastolatkiem.")
elif age > 20 and age < 65:
	print("Jesteś dorosły.")
elif age >= 65:
	print("Jesteś seniorem.")	


# Ćw 5.7 Ulubione owoce.

# Tworzymy listę z 3 ulubionymi owocami:
favourite_fruits = ['truskawka','kiwi','banan']
if "truskawka" in favourite_fruits:
	print("Naprawdę lubisz truskawki!")
if 'banan' in favourite_fruits:
	print("Naprawdę lubisz banany!")
if "kiwi" in favourite_fruits:
	print("Naprawdę lubisz kiwi!")
if 'ananas' in favourite_fruits:
	print("Naprawdę lubisz ananasy")			
