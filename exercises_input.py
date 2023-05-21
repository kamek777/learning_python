# Zrób to sam

# Ćw 7.1 Wypożyczenie samochodu

car = input('Jaki samochód chciałbyś wypożyczyć? ')
print(f'Chwileczkę, sprawdzę dostępność samochodu {car.upper()}.')

# Ćw 7.2 Stolik w restauracji 
reservetion = int(input("Ile miejsc chcesz zarezerwować w restauracji? "))

if reservetion > 8:
    print("Proszę zaczekać na wolne miejsca.")
else:
    print("Stolik gotowy!")    


# Ćw 7.3 Wielokrotność dziesięciu 

liczba = int(input("Wprowadź dowolną cyfrę a powiem Ci, czy jest wielokrotnością liczby 10 : "))

if liczba % 10 == 0:
    print(f"Tak, liczba {liczba} jest wielokrotnością liczby 10")
else:
    print(f"Niestety liczba {liczba} nie jest wielokrotnością liczby 10.")    