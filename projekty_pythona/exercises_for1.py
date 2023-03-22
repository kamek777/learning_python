# Zrób to sam 

# Ćw 5.1 Testy warunkowe

samochod = 'BMW'
print("Czy samochód to bmw? Przewiduję True.")
print(samochod=='bmw')
print("\n Czy samochód to audi? Przewiduję False.")
print(samochod=='audi')

# Ćw 5.2 Więcej testów warunkowych

# Sprawdzenie równości i nierówności ciągów tekstowych 
if samochod == 'BMW':
	print("True, it is bmw.")
else:
	print("False")	

if samochod !='audi':
	print("True, it is not audi.")
else:
	print("False")

if samochod == 'BMW':
	print(samochod.lower())
print(samochod=='BMW')	

if samochod =='BMW' and samochod!='audi':
	print(samochod=='BMW')
lista = ['pączek','karmel','masło']
print('pączek' in lista)
print('krem' not in lista)	
print('krem' in lista)