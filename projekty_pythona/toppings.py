requested_toppings = ['pieczarki','boczek','podwójny ser']
for requested_topping in requested_toppings:
	print(f"Dodaję {requested_topping}.")
print("\nTwoja pizza jest już gotowa!")	

# Sprawdzanie czy lista nie jest pusta:
requested_toppings1 = [] # pusta lista
if requested_toppings1:
	for requested_topping in requested_toppings1:
		print(f"Dodaję {requested_toppings1}.")
	print("\nTwoja pizza jest już gotowa!")
else:
 	print("Czy jesteś pewien, że chcesz pizzę bez składników?")		