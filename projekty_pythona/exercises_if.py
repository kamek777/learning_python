# Zrób to sam 

# Ćw 5.8 Witaj, administratorze

uzytkownicy = ['admin','gosc1','gosc2','gosc3','gosc4']

for uzytkownik in uzytkownicy:
	if uzytkownik == 'admin':
		print("Witaj, admin! Czy chcesz przejrzeć dzisiejszy raport?")
	else:
		print(f"Witaj, {uzytkownik.title()}! Dziękujemy, że ponownie się zalogowałeś.")	

# Ćw 5.9 Brak użytkowników

uzytkownicy1 = uzytkownicy[:] # kopiowanie listy 

if uzytkownik not in uzytkownicy1:
	print("Musimy znaleźć jakichś użytkowników.")
else:
	print("Na liście są użytkownicy.")

# Usuwanie listy:
n = len(uzytkownicy1)
for i in range(n):
	uzytkownicy1.pop()
	i+=1
# Sprawdzamy, czy jest faktycznie już pusta

print(uzytkownicy1)

# OK


if uzytkownik not in uzytkownicy1:
	print("Musimy znaleźć jakichś pracowników.")

# Ćw 5.10 Sprawdzanie nazw użytkowników 

current_users = ['michal123','kamil007','marcin_@11','justyna@_2221','marek332_@']
print(current_users)
new_users = ['mariusz990','franek_33@','lolek225','justyna@_2221','krol_445']
print(new_users)

for user in new_users:
	if user in current_users:
		print(f"Nie możesz użyć ten nazwy '{user}', jest już zajęta!")
	else:
		print(f"Możesz użyć tej nazwy '{user}'.")	


# Ćw 5.11 Liczby porządkowe 

# Lista 0-9:
lista = list(range(1,10))
print(lista)

# Iteracja przez listę

for element in lista:
	if element == 1:
		print("1st")
	elif element == 2:
		print("2nd")
	elif element == 3:
		print("3rd")
	elif element == 4:
		print("4th")
	elif element == 5:
		print("5th")
	elif element == 5:
		print("6th")
	elif element == 6:
		print("7th")
	elif element == 7:
		print("8th")
	else:
		print("9th")			