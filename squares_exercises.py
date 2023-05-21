# Zrób to sam

# Ćw 4.3 Odliczanie do dwudziestu 
listy = []
for lista in range(1,21):
	listy.append(lista)
print(listy)	

# Ćw. 4.4 Milion 
# Tworzenie listy od 1 do miliona
lista = list(range(1,1000001))
print(lista)
for element in lista:
	lista.append(element)
print(lista)	

# Ćw 4.5 Sumowanie do miliona
print("Suma listy to:",sum(lista))
print("Max listy to:",max(lista))
print("Min listy to:", min(lista))

#Ćw 4.6 Listy nieparzyste 
nieparzyste = []
for element in range(1,21,2):
	nieparzyste.append(element)
print(nieparzyste)	
# Ćw 4.7 Trzy
# Lista od 3 do 30 z elementami podniesionymi do potęgi trzeciej
trzecia_potega = [element**3 for element in range(3,31)]
print(trzecia_potega)

# Ćw 4.8 Sześcian
szescian = [element**3 for element in range(1,11)]
print(szescian)

# Inny sposób zapisania powyższego kodu
lista = []
for element in range(1,11):
	lista.append(element**3)
print(lista)	