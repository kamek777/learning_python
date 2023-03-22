# Kopiowanie listy 
my_foods = ['pizza','kebab','lasagne']
print(my_foods)
friends_foods = my_foods[:] # znak [:] kopiuje całą listę
print(friends_foods)

for food in my_foods[:]:
	print(f"{food.title()}\n")

for food in friends_foods[:]:
	print(f"{food.title()}\n")
