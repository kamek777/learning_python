# Zrób to sam

# Ćw 10.6. Dodawania
#try:
    #first_number = int(input("Wprowadź pierwszą liczbę: "))
    #second_number = int(input("Wprowadź drugą liczbę: "))
    #suma=first_number+second_number
    #print(f"Suma to: {suma}")
#except ValueError:
    #print("Proszę nie podawać ciągów znaków!")    
    
# Ćw 10.7. Kalkulator dodawania

import sys

#while True:
    #print("Jeśli chcesz przerwać wpisz 'q'.")
    #first_number = input("Wprowadź pierwszą liczbę: ")
    #second_number = input("Wprowadź drugą liczbę: ")
    #if first_number == 'q' or second_number == 'q':
    #        sys.exit()
    #try:
        #suma = int(first_number) + int(second_number)
        #print(f"Suma to: {suma}")
    #except ValueError:
        #pass
    
    
# Ćw 10.8. Koty i psy
filenames = ['dogs.txt','pliki_tekstowe/cats.txt']

def count_words(filename):
    try:
        with open(filename, encoding = 'utf-8') as f:
                contents = f.read()
    except FileNotFoundError:
        print("Podany plik {filename} nie istnieje!")            
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Plik {filename} zawiera {num_words} słów.")

for filename in filenames:
    count_words(filename)
    
        
           
    

    

            
        




        
    

