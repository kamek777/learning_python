from random import randint
from random import choice

kupon1 = [5, 3, 2, 1, 'k', 'l']
zbior_kupon1 = []
my_ticket = [1, 3, 'k']

flaga = True
zliczenia = 0
print(zbior_kupon1)

while flaga:
    zliczenia += 1
    for i in range(1, 4):
        losowanie = choice(kupon1)
        zbior_kupon1.append(losowanie)
    if my_ticket == zbior_kupon1:
        print(f"Wygrałeś, po {zliczenia} iteracjach.")
        flaga = False