# Zrób to sam 

# Ćw 7.8 Bar 

# Tworzymy listę z różnymi kanapkami 
sandwich_orders = ['kanapka z szynką','kanapka z kurczakiem','kanapka z salami','kanapka vege']

# Tworzymy pustą listę
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"Przygotowano: {sandwich}.")
    
while sandwich_orders:
    usuniety_element = sandwich_orders.pop()
    finished_sandwiches.append(usuniety_element)
    
for element in finished_sandwiches:
    print(element)        
    

# Ćw 7.9 Brak pastrami 
    
sandwich_orders = ['kanapka z szynką','kanapka z pastrami','kanapka z kurczakiem','kanapka z salami','kanapka z pastrami','kanapka vege','kanapka z pastrami']

print("Właśnie skończyło się pastrami! :( ")

# Usunięcie wszystkich elementów 'kanapka z pastrami' z listy sandwich_orders:

while 'kanapka z pastrami' in sandwich_orders:
    sandwich_orders.remove('kanapka z pastrami')
    
# Wyświetlenie listy 

print(sandwich_orders)  


# Ćw 7.10 Wymarzone wakacje

zbior = {}
flaga = True
while flaga:
    imie = input("Jak masz na imię:\n " )
    miejsce = input("Jeżeli mógłbyś odwiedzić jedno miejsce na ziemi co by to było?\n ")  
    zbior[imie] = miejsce
    zapytanie = input("Chcesz kontynuować? ('tak'/'nie')?\n ")    
    if zapytanie == 'nie':
        flaga = False

print("---Wynik ankiety---")

for imie,miejsce in zbior.items():
    print(f"{imie.title()} chce odwiedzić {miejsce.title()}.")        