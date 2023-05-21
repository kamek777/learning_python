# Zrób to sam 

# Ćw 9.13 Kości do gry 

from random import randint
from random import choice

class Die():
    """Klasa inicjująca grę w kości."""
    
    def __init__(self,sides=6):
        self.sides = sides
        
    def roll_die(self):
         self.rzut = randint(1,self.sides)
         return self.rzut
     
    def read_sides(self):
        return self.sides 

rzut1 = Die()
sixoczek = []
for i in range(1,11):
    los = rzut1.roll_die()
    print(los)
    sixoczek.append(los)
    
print(f"Oto zapisane rzuty dla liczby oczek {rzut1.read_sides()} : {sixoczek}")   

# Ćw 9.14 Loteria
kupon1 = [7,5,3,4,8,2,1,10,12,15,'k','l','c','m']
kupon2 = (7,4,8,1,2,3,5,6,9,11,'i','o','p')
zbior_kupon1 = []
for i in range(1,5):
    losowanie = choice(kupon1)
    zbior_kupon1.append(losowanie)
zbior_kupon2 = []   
for i in range(1,5):
    losowanie = choice(kupon2)
    zbior_kupon2.append(losowanie) 
    
print(f"Oto liczby lub litery, które wygrywają kupon: {zbior_kupon1}")
print(f"Oto liczby lub litery, które wygrywają kupon: {zbior_kupon2}")

# Ćw 9.15 Analiza loterii

# Tworzymy własny kupon i iterujemy do momentu, gdy trafimy cały klucz oraz wyświetlimy po ilu 
# iteracjach się to udało.

my_ticket = [1,3,5,'k']
zliczenia = 0 
flaga = True

while flaga:
    zliczenia += 1
    if my_ticket == zbior_kupon1:
        print(f"Wygrałeś, po {zliczenia} iteracjach.")
        flaga = False
    


    
    
