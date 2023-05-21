# Zrób to sam 

# Ćw 4.10 Wycinki

# Tworzymy dowolną listę
owoce = ['jabłko','banan','gruszka','śliwka','granat']


print(f"Pierwsze trzy elementy listy to: \n{owoce[:3]}")
print(f"Trzy elementy w środku listy to: \n {owoce[1:4]}")
print(f"Ostanie trzy elementy listy to: \n {owoce[2:]}")

# Ćw 4.11 Moja pizza, Twoja pizza
my_pizzas = ['pepperoni', 'salami', 'hawajska','margharita']
friend_pizzas = my_pizzas[:] # Tworzenie kopii listy 
print(my_pizzas)
print(friend_pizzas)
my_pizzas.append('mięsna_uczta')
friend_pizzas.append('vege')
print("Moje ulubione pizze to:\n")
for pizza in my_pizzas[:]:
	print(pizza.title())

print("Ulubione rodzaje pizzy mojego przyjaciela to:\n")
for pizza in friend_pizzas[:]:
	print(pizza.title())