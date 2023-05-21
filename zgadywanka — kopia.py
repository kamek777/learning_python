# Zgadywanka
import random
status= True

while status:
    guess = int(input("Podaj losową liczbę id 1 do 8: "))
    i = random.randint(1, 9)
    if i == guess:
        print("Wow, naprawdę to zrobiłeś!")
        print("Poprawna odpowiedź :)")
    elif guess>= i+3:
        print("Stanowczo za duża liczba")
    elif guess<= i-3:
        print("Stanowczo za mała liczba")
    else: 
        print("Prawie się udało!")
        print(i)
    check=input("Chcesz wyjść? napisz koniec, jesli nie to wpisz cokolwiek:").lower()
    if check == "koniec":
        status=False
    else:
        continue
        
        
        
    
    
