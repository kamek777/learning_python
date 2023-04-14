# Zrób to sam 

# Ćw 10.3. Gość
#imie = input("Podaj swoje imię: ")
filename = 'pliki_tekstowe/guest_book.txt'
#with open(filename,'w') as file_object:
    #file_object.write(imie)
    
# Ćw 10.4. Księga gości 
print("Jeśli chcesz zakończyć, napisz 'koniec'.")


while imie!='koniec':
    imie = input("Podaj imię: ")
    with open(filename, 'a') as file_object:
        file_object.write(imie.title() + '\n')
    print(f"Witaj, {imie.title()}!\n")


    
    


        