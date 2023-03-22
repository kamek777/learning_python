# Zrób to sam 

# Ćw 7.4 Dodatki do pizzy

polecenie = "Jakie dodatki chcesz umieścić w pizzy? "
polecenie += "Chcesz coś jeszcze umieścić? Jeśli nie to wpisz 'koniec'. "
message = ""
while message != 'koniec':
    message = input(polecenie)
    print(f"Dodałeś składnik: {message}")
    if message == 'koniec':
        break


# Ćw 7.5 Bilety do kina

age = int(input("Podaj swój wiek: "))
active = True
while active:
    if age < 3:
        print(f"Dzieci w wieku {age} mają bezpłatne wejście!" )
        break
    elif age >= 3 and age <= 12:
        print(f"Bilet w Twoim wieku {age} lat kosztuje 10 zł. ") 
        break   
    elif age > 12:
        print(f"Bilet dla Ciebie w wieku {age} kosztuje 15zł. ")
        break   
    else:
        active = False
# Ćw 7.6 Trzy wyjścia

# Wszystko zawarłem we wcześniejszych programach :)


# Ćw 7.7 Nieskończoność 

#liczba = 1 
#while liczba < 5:
#    print(liczba)  

# Przerywamy nieskończoną pętlę poleceniem CTRL + C      